
function setImagem(valor) {
     document.getElementById("link_imagem").value = `https://www.themoviedb.org/t/p/w600_and_h900_bestv2${valor}`;
     document.getElementById('poster').setAttribute('src', `https://www.themoviedb.org/t/p/w600_and_h900_bestv2${valor}`);
}

//  pegar dados dos filmes pelo TMDB
const limparCampos = () => {
     document.getElementById('titulo_original').value = '';
     document.getElementById('titulo_traduzido').value = '';
     document.getElementById('imdb').value = '';
     document.getElementById('data_release').value = '';
     document.getElementById('sinopse').value = '';
     document.getElementById('link_imagem').value = '';
     document.getElementById('poster').setAttribute('src', 'https://colorindo.org/wp-content/uploads/2022/10/desenhos-de-ponto-de-interrogacao-1.jpg');
     document.getElementById("tblPosters").innerHTML = "";
}

const populaPosters = async () =>{
     const tmdb = document.getElementById('tmdb').value;
     const url2 = 'https://api.themoviedb.org/3/movie/' + tmdb + '/images?api_key=2b0120b7e901bbe70b631b2273fe28c9';
     const dados2 = await fetch(url2);
     const elemento2 = await dados2.json();

     let tabela = document.getElementById("tblPosters")
     let linha = document.createElement("tr")

     for (let key in elemento2.posters) {

          th = document.createElement("th")
          th.innerHTML = "<a href='#'><img width='100px' src='https://image.tmdb.org/t/p/w600_and_h900_bestv2" + elemento2.posters[key].file_path + "' onclick=setImagem('" + elemento2.posters[key].file_path + "')></a>"
          linha.appendChild(th)
     }

     tabela.appendChild(linha)
}

const pesquisaImdb = async () => {
     limparCampos();
     const tmdb = document.getElementById('tmdb').value;
     const url = `https://api.themoviedb.org/3/movie/${tmdb}?api_key=2b0120b7e901bbe70b631b2273fe28c9&language=pt-BR&include_adult=false`;
     const dados = await fetch(url);
     const elemento = await dados.json();
     if (elemento.hasOwnProperty('success')) {
          document.getElementById('tmdb').value = -1;
     } else {
          document.getElementById('titulo_original').value = elemento.original_title.toUpperCase();
          document.getElementById('titulo_traduzido').value = elemento.title.toUpperCase();
          document.getElementById('imdb').value = elemento.imdb_id;
          document.getElementById('data_release').value = elemento.release_date;
          document.getElementById('sinopse').value = elemento.overview;
          document.getElementById('link_imagem').value = `https://www.themoviedb.org/t/p/w600_and_h900_bestv2${elemento.poster_path}`;
          document.getElementById('poster').setAttribute('src', `https://www.themoviedb.org/t/p/w600_and_h900_bestv2${elemento.poster_path}`);
     }
     populaPosters();
}

document.getElementById('tmdb').addEventListener('focusout', pesquisaImdb);
// ate aqui

const troca_imagem = async () => {
     document.getElementById("poster").src = document.getElementById("link_imagem").value;
}
document.getElementById('link_imagem').addEventListener('focusout', troca_imagem);

// Mascara de Data
//const element = document.getElementById('data_release');
//const maskOptions = {
//  mask: '0000-00-00'
//};
//const mask = IMask(element, maskOptions);
// ate aqui