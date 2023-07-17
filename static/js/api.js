const limparCampos = () => {
        document.getElementById('titulo_original').value = '';
        document.getElementById('titulo_traduzido').value = '';
        document.getElementById('imdb').value = '';
        document.getElementById('data_release').value = '';
        document.getElementById('sinopse').value = '';
        document.getElementById('link_imagem').value = '';
        document.getElementById('poster').setAttribute('src', 'https://colorindo.org/wp-content/uploads/2022/10/desenhos-de-ponto-de-interrogacao-1.jpg');
}

const pesquisaImdb = async () => {
   limparCampos();
   const tmdb = document.getElementById('tmdb').value;
   const url = `https://api.themoviedb.org/3/movie/${tmdb}?api_key=2b0120b7e901bbe70b631b2273fe28c9&language=pt-BR&include_adult=false`
   const dados = await fetch(url);
   const elemento = await dados.json();
   if(elemento.hasOwnProperty('success') ){
        document.getElementById('tmdb').value = -1;
   } else {
        document.getElementById('titulo_original').value = elemento.original_title;
        document.getElementById('titulo_traduzido').value = elemento.title;
        document.getElementById('imdb').value = elemento.imdb_id;
        document.getElementById('data_release').value = elemento.release_date;
        document.getElementById('sinopse').value = elemento.overview;
        document.getElementById('link_imagem').value = `https://www.themoviedb.org/t/p/w600_and_h900_bestv2${elemento.poster_path}`;
        document.getElementById('poster').setAttribute('src',`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${elemento.poster_path}`);
   }
}

const imdb =  document.getElementById('tmdb').addEventListener('focusout', pesquisaImdb );


const troca_imagem = async () => {
    document.getElementById("poster").src = document.getElementById("link_imagem").value ;
}
document.getElementById('link_imagem').addEventListener('focusout', troca_imagem );