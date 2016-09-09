// This is the custom JavaScript file referenced by index.html. You will notice
// that this file is currently empty. By adding code to this empty file and
// then viewing index.html in a browser, you can experiment with the example
// page or follow along with the examples in the book.
//
// See README.txt for more information.

$('document').ready(function() {
	var $speech = $('div.speech');
	$('#switcher button').on('click',function() {
		var num = parseFloat($speech.css('fontSize'));
		if(this.id == 'switcher-large') {
			num *= 1.4;
		}
		else if(this.id == 'switcher-small') {
			num /= 1.4;
		}
		$speech.css('fontSize',num + 'px');
	});
	var $firstPara = $('p').eq(1);
	$firstPara.hide();
	$('a.more').click(function(event) {
		event.preventDefault();
		$firstPara.animate({height: 'toggle'},'slow');
		var $link = $(this);
		if($link.text() == 'read more') {
			$link.text('read less')
		}
		else {
			$link.text('read more');
		}
	});
});