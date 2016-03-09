

$(document).ready( function() {

	// for drawing page ---------

	//when submit_search button clicked
	$('#submit_search').click(function(event){
		var searchFilm = $("#film_search").val(); //value to search for is value in searchFilm box

		//AJAX request to OMDB API
    $.getJSON('http://www.omdbapi.com/?s=' + searchFilm, function(json_data){
		$('#options option').remove(); //remove any previous options on the dropdown
		for (var i = 0; i < json_data.Search.length; i++) { //loop through JSON results and append to options
		$('#options').append('<option value="' + json_data.Search[i].Title + '">' + json_data.Search[i].Title + '</option>');
		}
    });
	//unhide the options box if hidden(default)
	$("#options").show();
	//clear the search box for next input
	$("#film_search").val('');
});

$("#options").on("change", function() {
      $("#id_film").val($(this).val());
    });



	//for likes ----------
	$(document).on("click","#like", function(){
		var catid;
		catid = $(this).attr("data-catid");
		$.get('/drawflix/like_drawing/', {drawing_id: catid}, function(data){
							 location.reload();
    });

	});

	var myBoard = new DrawingBoard.Board('test_board');

	$("#Test").click(function() {
		
		var canvas = myBoard.getImg();
		
		$("#id_image").val(canvas);



});

});
