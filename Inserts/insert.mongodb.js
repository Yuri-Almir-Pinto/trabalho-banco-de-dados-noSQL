/* Conecta ao mongodb atlas e carrega os dados de municipios */
// conecta ao banco de dados geo
use('db_provas'); 

// salva numa variavel a coleção municipios
let questoes = db.getCollection('provas');

// apaga todos os documentos de municipios antes de importar os novos
questoes.drop();

// importa api do Nodejs para ler arquivos:
const fs = require('fs');
let rawdata = fs.readFileSync('Inserts/provas.json');
// converte o conteudo do arquivo para um objeto javascript (data):
let data = JSON.parse(rawdata);
console.log('Total livros carregados do arquivo: ' + data.length);

console.log('Inserindo Documentos no cloud atlas...');
questoes.insertMany(data);
console.log('Total Documentos inseridos: ' + questoes.countDocuments() + ' livros.');
// abrir cloud atlas e verificar se os documentos foram inseridos na
// base de dados "geo" -> coleção "municipios"

// teste: primeiro Documento da Coleção é... "Alta Floresta D'Oeste"
let doc1 = questoes.findOne();
console.log(JSON.stringify(doc1, null, 2))