$(document).ready(function () {
    $.getJSON('https://saurav.tech/NewsAPI/top-headlines/category/technology/us.json', function (data) {
        console.log(data)
        $('seccionNoticia').hide();

    }).fail(function () {
        $('#spinnerNoticia').hide();
        $('seccionNoticia').show();
        $('#textoNoticia').text("Error el cargar noticia.");

    }).done(function(data){
        $('#textoNoticia').text("" + data.articles[1].description);
        $('#headerNoticia').text("" + data.articles[1].title);
        $('#noticiaImagen').attr("src",data.articles[1].urlToImage);
        $('#linkNoticia').attr("href",data.articles[1].url);
        $('#spinnerNoticia').hide();
        $('seccionNoticia').show();
    });
});