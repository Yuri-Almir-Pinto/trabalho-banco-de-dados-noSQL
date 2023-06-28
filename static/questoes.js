function toggle(element, id) {
    var questoes = document.getElementById(id);
    var simbolos = {
      "[+]": "[-]",
      "[-]": "[+]"
    };
  
    questoes.style.display = (questoes.style.display === "none") ? "block" : "none";
    element.innerHTML = element.innerHTML.replace(/\[.\]/, function(encontrado) {
        return simbolos[encontrado];
    });

}

function adicionarAlternativa() {
    var element = document.getElementById("alternativas-div");

    var div = document.createElement("div");
    div.className = "input-group mb-3";

    var input = document.createElement("input");
    input.type = "text";
    input.className = "form-control";
    input.setAttribute("aria-label", "Alternativa");
    input.setAttribute("aria-describedby", "button-addon1");
    input.name = "alternativas";
    input.required = true;

    var button = document.createElement("a");
    button.title = "editar";
    button.className = "btn btn-danger";
    button.type = "button";
    button.addEventListener("click", function() {
        removerCampo(this);
    });

    var divRadio = document.createElement("div");
    divRadio.className = "input-group-text"

    var radio = document.createElement("input");
    radio.className = "form-check-input mt-0";
    radio.type = "radio";
    radio.ariaLabel = "Correta";
    radio.name = "correta";
    radio.required = true;

    var icon = document.createElement("i");
    icon.className = "bi bi-x-circle";

    button.appendChild(icon);
    divRadio.appendChild(radio);
    div.appendChild(divRadio);
    div.appendChild(input);
    div.appendChild(button);
    element.appendChild(div);

    countRadios();
}

function adicionarTexto() {
    var element = document.getElementById("textos-div");

    var div = document.createElement("div");
    div.className = "info-group mb-3";

    var inputDescricao = document.createElement("input");
    inputDescricao.type = "text";
    inputDescricao.className = "form-control";
    inputDescricao.setAttribute("aria-label", "Texto");
    inputDescricao.name = "descricaoTexto";
    inputDescricao.placeholder = "Descrição do Texto"
    inputDescricao.required = true;

    var inputLink = document.createElement("input")
    inputLink.type = "text";
    inputLink.className = "form-control";
    inputLink.setAttribute("aria-label", "Link");
    inputLink.name = "linkTexto";
    inputLink.placeholder = "Link do Texto"
    inputLink.required = true;

    var button = document.createElement("a");
    button.title = "Remover";
    button.className = "btn btn-danger";
    button.type = "button";
    button.addEventListener("click", function() {
        removerCampo(this);
    });

    var icon = document.createElement("i");
    icon.className = "bi bi-x-circle";

    button.appendChild(icon);
    div.appendChild(inputLink);
    div.appendChild(inputDescricao);
    div.appendChild(button);
    element.appendChild(div);
}

function adicionarImagem() {
    var element = document.getElementById("imagens-div");

    var div = document.createElement("div");
    div.className = "info-group mb-3";

    var inputDescricao = document.createElement("input");
    inputDescricao.type = "text";
    inputDescricao.className = "form-control";
    inputDescricao.setAttribute("aria-label", "Imagem");
    inputDescricao.name = "descricaoImagem";
    inputDescricao.placeholder = "Descrição da Imagem"
    inputDescricao.required = true;

    var inputLink = document.createElement("input")
    inputLink.type = "text";
    inputLink.className = "form-control";
    inputLink.setAttribute("aria-label", "Link");
    inputLink.name = "linkImagem";
    inputLink.placeholder = "Link da Imagem"
    inputLink.required = true;

    var button = document.createElement("a");
    button.title = "Remover";
    button.className = "btn btn-danger";
    button.type = "button";
    button.addEventListener("click", function() {
        removerCampo(this);
    });

    var icon = document.createElement("i");
    icon.className = "bi bi-x-circle";

    button.appendChild(icon);
    div.appendChild(inputLink);
    div.appendChild(inputDescricao);
    div.appendChild(button);
    element.appendChild(div);
}

function adicionarTopico() {
    var element = document.getElementById("topicos-div");

    var div = document.createElement("div");
    div.className = "input-group mb-3";

    var input = document.createElement("input");
    input.type = "text";
    input.className = "form-control";
    input.setAttribute("aria-label", "Tópico");
    input.setAttribute("aria-describedby", "button-addon2");
    input.name = "topicos";
    input.required = true;

    var button = document.createElement("a");
    button.title = "Remover";
    button.className = "btn btn-danger";
    button.type = "button";
    button.addEventListener("click", function() {
        removerCampo(this);
    });

    var icon = document.createElement("i");
    icon.className = "bi bi-x-circle";

    button.appendChild(icon);
    div.appendChild(input);
    div.appendChild(button);
    element.appendChild(div);
}

function removerCampo(element) {

    var parent = element.parentNode;

    parent.remove();
}

function countRadios() {
    var radios = document.querySelectorAll("#alternativas-div input[type='radio']");
    var  num = 0;
    radios.forEach(element => {
        element.value = num;
        num += 1;
    });
}