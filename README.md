# Criar projeto

```bash
mkdir appbook && cd
python3 -m venv env --without-pip --system-site-packages
source env/bin/activate
pip install Flask
pip install pymongo
pip install flask
pip install python-dotenv
```

## Adicionar arquivo `.env`

Na pasta raiz do projeto `appbook/.env`

Este arquivo armazena configurações, como a url de conexão com o banco de dados.

```bash
CLUSTER_URL=mongodb+srv://USER:PASSWORD@cluster0.srvern.mongodb.net/test
```

## Teste de conexão

```bash
python3 test_connection.py
```
