$(document).ready( function() {
	
	$('#submit_search').click(function(event){
		var searchFilm = $("#film_search").val();
				
    $.getJSON('http://www.omdbapi.com/?s=' + searchFilm, function(json_data){
		$('#options option').remove();
		for (var i = 0; i < json_data.Search.length; i++) {
		$('#options').append('<option value="' + json_data.Search[i].Title + '">' + json_data.Search[i].Title + '</option>');
		}
    });
	
	$("#options").show();
});
	
	
});			



