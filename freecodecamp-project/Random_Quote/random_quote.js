$(document).ready(function() {
    
	var quote;//store the quote
    $('#get_quote').on('click', function() {
        $.ajax({
            //using the jsonp to cross the domain
            url: "https://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1&_jsonp=mycallback",
            dataType: 'jsonp',
            crossDomain: true,
            //the custom callback function
            jsonpCallback:'mycallback',
            success: function(data) {
            	console.log(data);
            	quote=data[0];
            	//replace the content
            	$("#author").text(quote.title),
                $("#quote_text").html(quote.content)
            }
            
        });
    });
   

});