from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_Headers'] = 'Content-Type'


def get_db():
    client = MongoClient(host='mongodb',
                         port=27017,
                         username='root',
                         password='pass',
                         authSource="admin")
    db = client["cloudopss_db"]
    return db


@app.route('/')
def ping_server():
    return "API CloudOpss"


@app.route('/clients', methods=['GET'])
@cross_origin()
def get_stored_clients():
    db = ""
    try:
        db = get_db()
        clientList = db.client_tb.find()
        clients = [{"id": client["id"], "name": client["name"],
                    "email": client["email"], "phone": client["phone"],
                    "address": client["address"], "profession": client["profession"]}
                    for client in clientList]
        return jsonify({"clients": clients})
    except:
        pass
    finally:
        if type(db) == MongoClient:
            db.close()


@app.route('/clients', methods=['POST'])
@cross_origin()
def post_stored_clients():
    db = ""
    try:
        db = get_db()

        id = request.json['id']
        name = request.json['name']
        email = request.json['email']
        phone = request.json['phone']
        address = request.json['address']
        profession = request.json['profession']
        clients = [{"id": id, "name": name, "email": email,
                    "phone": phone, "address": address, "profession": profession}]
        db.client_tb.insert_many(clients)
        return jsonify({"clients": {"id": id, "name": name, "email": email, "phone": phone, "address": address, "profession": profession}})
    except:
        pass
    finally:
        if type(db) == MongoClient:
            db.close()


@app.route('/clients/delete/<name>', methods=['DELETE'])
def delete_stored_clients(name):
    db = ""
    try:
        clientList = list()
        db = get_db()
        db.client_tb.delete_one({"name": name})
        for i in db.client_tb.find():
            clientList.append(
                {"id": i["id"], "name": i["name"], "email": i["email"], "phone": i["phone"], "address": i["address"], "profession": i["profession"]})
        return jsonify(clientList)
    except:
        pass
    finally:
        if type(db) == MongoClient:
            db.close()


@app.route('/clients/update/<name>', methods=['PUT'])
def update_stored_clients(name):
    db = ""
    try:
        clientList = list()
        db = get_db()
        updatedName = request.json['name']
        db.client_tb.update_one(
            {'name': name}, {"$set": {'name': updatedName}})
        for i in db.client_tb.find():
            clientList.append(
                {"id": i["id"], "name": i["name"], "email": i["email"], "phone": i["phone"], "address": i["address"], "profession": i["profession"]})
        return jsonify(clientList)
    except:
        pass
    finally:
        if type(db) == MongoClient:
            db.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
