//para mostrar apenas uma variavel, tipo o titulo = .titulo
//para voce comentar uma variavel no arquivo para html usa ${dados[0].titulo}

function pesquisar() {
    //console.log(dados);
    //document.getElementById = dentro do arquivo html buscar pelo id ("")
    // Busca a seção onde os resultados serão exibidos.
    // O elemento com o ID "resultados-pesquisa" será o container para os resultados.
    let section = document.getElementById("resultados-pesquisa");


    let campoPesquisa = document.getElementById("campo-pesquisa").value 
    if (!campoPesquisa) {
        section.innerHTML = "<p> Nada foi encontrado. Você precisa digitar algo ... </p>"
        return
    }

    campoPesquisa = campoPesquisa.toLowerCase()


    // Inicializa uma string vazia para armazenar os resultados formatados em HTML.
    let resultados = "";
    let titulo = "";
    let descricao = "";
    let tags = "";

    // Itera sobre cada item (dado) da lista de dados (provavelmente um array).
    // Para cada dado, cria um novo elemento HTML com as informações do resultado.
    //para cada dado dentro da lista de dados.
    for (let dado of dados) {

        titulo = dado.titulo.toLowerCase()
        descricao = dado.descricao.toLowerCase()
        tags = dado.tags.toLowerCase()
        //se titulo includes campoPesquisa
        //então, faça ...
        if (titulo.includes(campoPesquisa) || descricao.includes(campoPesquisa) || tags.includes(campoPesquisa)) {
            // Constrói uma string de HTML para cada resultado, incluindo:
            // - Um título (h2) com um link para mais informações.
            // - Uma descrição (p) com a classe "descricao-meta".
            // - Um link para mais informações.
            resultados += `
            <div class="item-resultado">
                <h2>
                    <a href="#" target="_blank"> ${dado.titulo} </a>
                </h2>
                <p class="descricao-meta">${dado.descricao} </p>
                <a href=${dado.link}  target="_blank">Mais informações</a>
            </div> 
         `;
        }
    }

    if (!resultados) {
        resultados = "<p> Nada foi encontrado </p>"
    }

    // Atribui a string com todos os resultados ao conteúdo HTML da seção.
    // Isso substitui o conteúdo anterior da seção pelos novos resultados.
    section.innerHTML = resultados;
}





// foto perfil 

const uploadPhoto = document.getElementById('upload-photo');

uploadPhoto.addEventListener('change', () => {
    const reader = new FileReader();
    reader.onload = (e) => {
        document.getElementById('profile-pic').src = e.target.result;
    };
    reader.readAsDataURL(uploadPhoto.files[0]);
});