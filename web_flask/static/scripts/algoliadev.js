window.onload = function() {
    var client = algoliasearch('RJE7GLL1FV', 'ad5ce4237e556dced555fa4f18424a86');

    var index = client.initIndex('dev_MEMES')

    $('button').click(function() {
	$('.meme_container').empty();
	let searchterm = $('input[type=text][name=search]').val();
	console.log(searchterm)
	if (searchterm === null || searchterm === "")
	{
	    window.location.reload();
	} else {
	    index.search(searchterm, function(err, content) {
		if (err) {
		    console.error(err);
		} else {
		    $(content.hits).each(function () {
			$('.meme_container').append($('<div class="img_box">')
						    .append('<div class="image"><img src="' + $(this).attr('url') + '" </div>')
						    .append('<p>' + $(this).attr('name') + '</p>'))
			console.log($(this).attr('name'));
		    });
		}
	    });
	}
    });
};
