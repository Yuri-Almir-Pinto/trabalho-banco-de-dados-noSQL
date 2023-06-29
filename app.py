from flask import (
    Flask, render_template, request, redirect, url_for, flash
)
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os, DaoProvas, DaoQuestoes, entities
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdf0001'

cluster_url = os.getenv("CLUSTER_URL")
cluster = MongoClient(cluster_url)


def get_provas():
    db = cluster["db_provas"]
    collection = db["provas"]
    return collection

def get_questoes():
    db = cluster["db_provas"]
    collection = db["questoes"]
    return collection

def instanciarProva(request):
    id = request.form.get("id")
    cargo = request.form.get("cargo")
    ano = request.form.get("ano")
    orgao = request.form.get("orgao")
    instituicao = request.form.get("instituicao")
    nivel = request.form.get("nivel")
    prova = entities.Prova(cargo, ano, orgao, instituicao, nivel, id = id)

    return prova

def instanciarQuestao(request):
    id = request.form.get("id")
    enunciado = request.form.get("enunciado")

    alternativas = request.form.getlist("alternativas")
    corretas = request.form.get("correta")
    qAlternativas = []

    for i in range(len(alternativas)):
        if i == int(corretas):
            qAlternativas.append(entities.Alternativas(alternativas[i], True))
        else:
            qAlternativas.append(entities.Alternativas(alternativas[i], False))

    linkTexto = request.form.getlist("linkTexto")
    descricaoTexto = request.form.getlist("descricaoTexto")
    qTexto = []

    for i in range(len(linkTexto)):
        qTexto.append(entities.Info(descricaoTexto[i], linkTexto[i]))

    linkImagem = request.form.getlist("linkImagem")
    descricaoImagem = request.form.getlist("descricaoImagem")
    qImagem = []

    for i in range(len(linkImagem)):
        qImagem.append(entities.Info(descricaoImagem[i], linkImagem[i]))

    topicos = request.form.getlist("topicos")
    qTopico = []

    for topico in topicos:
        qTopico.append(topico)

    
    final = entities.Questoes(qTopico, enunciado, qAlternativas, qTexto, qImagem, id = id)

    return final

# ==================================
# ROTAS
# ==================================


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/provas/index", methods=["GET"])
def provas_index():
    provas = DaoProvas.readAll()
    return render_template("provas_list.html", provas=provas)

@app.route("/questoes/index", methods=["GET", "POST"])
def questoes_index():
    if request.method == "GET":
        questoes = DaoQuestoes.readAll()
        return render_template("questoes_list.html", questoes=questoes)
    
    selecionado = request.form.get('filtro')
    texto = request.form.get('filtroTexto')
    questoes = DaoQuestoes.filtrarEnunciadoTags(selecionado, texto)
    
    return render_template("questoes_list.html", questoes = questoes)

@app.route("/provas/create", methods=["GET", "POST"])
def provas_create():
    if request.method == "GET":
        return render_template("provas_update_create.html", action="create")

    prova = instanciarProva(request)

    if DaoProvas.create(prova):
        flash(f"Prova criada com sucesso!")
    else:
        flash(f"Erro ao criar prova.")

    return redirect(url_for("provas_index"))

@app.route("/questoes/create", methods=["GET", "POST"])
def questoes_create():
    if request.method == "GET":
        return render_template("questoes_update_create.html", action="create")

    result = instanciarQuestao(request)

    if DaoQuestoes.create(result):
        flash(f"Questão criada com sucesso!", "success")
    else:
        flash(f"Erro ao criar questão.", "warning")

    return redirect(url_for("questoes_index"))
        

@app.route("/provas/update/<id>", methods=["GET", "POST"])
def provas_update(id):
    if request.method == "GET":
        prova = DaoProvas.read(id)
        return render_template("provas_update_create.html", prova = prova, action="update")

    prova = instanciarProva(request)

    if DaoProvas.update(prova):
        flash(f"Prova atualizada com sucesso!", "success")
    else:
        flash(f"Erro ao atualizar a prova.", "warning")

    return redirect(url_for("provas_index"))

@app.route("/provas/questoes/redirect/<idProva>/<action>", methods=["GET"])
@app.route("/provas/questoes/redirect/<idProva>/<action>/<idQuestao>", methods=["GET"])
def provas_redirect(idProva, action, idQuestao = None):
    if action == "edit":
        prova = DaoProvas.read(idProva)
        questoes = DaoQuestoes.getAllQuestoes(prova["questoes"])
        return render_template("questoes_list.html", prova = prova, questoes = questoes)

    if action == "remover":
        DaoProvas.removerQuestao(idProva, idQuestao)
        prova = DaoProvas.read(idProva)
        questoes = DaoQuestoes.getAllQuestoes(prova["questoes"])
        return render_template("questoes_list.html", prova = prova, questoes = questoes)

    return render_template("provas_update_create.html", prova = prova, action="update")

@app.route("/questoes/update/<id>", methods=["GET", "POST"])
def questoes_update(id):
    if request.method == "GET":
        questao = DaoQuestoes.read(id)
        return render_template("questoes_update_create.html", questoes = questao, action="update")

    questao = instanciarQuestao(request)

    if DaoQuestoes.update(questao):
        flash(f"Questao atualizada com sucesso!", "success")
    else:
        flash(f"Erro ao atualizar a questao.", "warning")

    return redirect(url_for("questoes_index"))

@app.route("/provas/delete/<id>", methods=["GET"])
def provas_delete(id):
    if DaoProvas.delete(id):
        flash(f"Prova deletada com sucesso.", "success")
    else:
        flash(f"Erro ao tentar deletar prova.", "warning")
    return redirect(url_for('provas_index'))

@app.route("/questoes/delete/<id>", methods=["GET"])
def questoes_delete(id):
    if DaoQuestoes.delete(id):
        flash(f"Questão deletada com sucesso.", "success")
    else:
        flash(f"Erro ao tentar deletar questão.", "warning")
    return redirect(url_for('questoes_index'))

if __name__ == "__main__":
    app.run(debug=True)
