$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    data.results.forEach(element => {
        $('<li>'+ element.title + '</li>').appendTo('UL#list_movies');
    });
});