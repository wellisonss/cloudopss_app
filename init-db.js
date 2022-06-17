db = db.getSiblingDB("cloudopss_db");
db.client_tb.drop();

db.client_tb.insertMany([
    {
        "id": 1,
        "name": "Mirela",
        "email": "mirela@gmail.com",
        "phone": "988888888",
        "address": "rua nao sei doq",
        "profession": "desempregada"
    },
    {
        "id": 2,
        "name": "Wellison",
        "email": "wellison@gmail",
        "phone": "987777777",
        "address": "rua 10",
        "profession": "desempregado"
    },
]);