import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os, json

cluster_url = os.getenv("CLUSTER_URL")

def getCollection():
    cluster = MongoClient(cluster_url)
    db = cluster["db_provas"]
    collection = db["questoes"]
    return collection

def getQuestaoJson(questao):
    questaoJson = {
        "topicos": [],
        "enunciado": questao.enunciado,
        "alternativas": [],
        "textos": [],
        "imagens": []
    }

    for topico in questao.topicos:
        questaoJson["topicos"].append(topico)

    for alternativa in questao.alternativas:
        alternativaJson = {
            "enunciado": alternativa.enunciado,
            "correta": alternativa.correta
        }

        questaoJson["alternativas"].append(alternativaJson)

    for texto in questao.textos:
        textoJson = {
            "descricao": texto.descricao,
            "link": texto.link
        }

        questaoJson["textos"].append(textoJson)

    for imagem in questao.imagens:
        imagensJson = {
            "descricao": imagem.descricao,
            "link": imagem.link
        }

        questaoJson["imagens"].append(imagensJson)

    return questaoJson

def create(questao):
    collection = getCollection()

    questaoJson = getQuestaoJson(questao)

    collection.insert_one(questaoJson)

    return True

def update(questao):
    collection = getCollection()
    questaoJson = getQuestaoJson(questao)

    collection.update_one({
        "_id": ObjectId(questao.id)
    }, 
    {
        "$set": questaoJson
    })

    return True

def read(id):
    collection = getCollection()

    result = collection.find_one({
        "_id": ObjectId(id)
    })

    return result

def delete (id):
    collection = getCollection()
    collection.delete_one(
        {"_id": ObjectId(id)}
        )
    return True

def readAll ():
    collection = getCollection()
    result = collection.find()
    return list(result)

def getAllQuestoes (ids):
    questoes = []
    for id in ids:
        questoes.append(ObjectId(id))
    
    collection = getCollection()
    result = collection.find({"_id": {
        "$in": questoes
    }})
    return list(result)