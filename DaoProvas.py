import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

cluster_url = os.getenv("CLUSTER_URL")

def getCollection():
    cluster = MongoClient(cluster_url)
    db = cluster["db_provas"]
    collection = db["provas"]
    return collection

def getProvaJson(prova):
    provaJson = {
        "cargo": prova.cargo,
        "ano": prova.ano,
        "orgao": prova.orgao,
        "instituicao": prova.instituicao,
        "nivel": prova.nivel,
        "questoes": []
    }

    for questao in prova.questoes:

        provaJson["questoes"].append(questao)

    return provaJson

def create(prova):
    collection = getCollection()

    provaJson = getProvaJson(prova)

    collection.insert_one(provaJson)

    return True

def read(id):
    collection = getCollection()

    result = collection.find_one({
        "_id": ObjectId(id)
    })

    return result

def update(prova):
    collection = getCollection()
    provaJson = getProvaJson(prova)

    collection.update_one({
        "_id": ObjectId(prova.id)
    }, 
    {
        "$set": provaJson
    })

    return True


def delete(id):
    collection = getCollection()
    collection.delete_one(
        {"_id": ObjectId(id)}
        )
    return True

def readAll():
    collection = getCollection()
    result = collection.find()
    return list(result)

def removerQuestao(idProva, idQuestao):
    collection = getCollection()
    collection.update_one({
        "_id": ObjectId(idProva)
    }, {
        "$pull": {
            "questoes": idQuestao
        }
    })