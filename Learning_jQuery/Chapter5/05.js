// This is the custom JavaScript file referenced by index.html. You will notice
// that this file is currently empty. By adding code to this empty file and
// then viewing index.html in a browser, you can experiment with the example
// page or follow along with the examples in the book.
//
// See README.txt for more information.

$(document).ready(function() {
    $('div.chapter a').click(function(event) {
        event.preventDefault();
        $('div.chapter a[href*="wikipedia"]').attr({
            rel: 'external',
            title: function() {
                return 'Learn more about ' + $(this).text() + ' at wikipedia.';
            },
            id: function(index, oldValue) {
                return 'wikilink-' + index;
            }
        });
    });
    $('<a href="#top">bact to top</a>').insertAfter('div.chapter p');
    $('<a id="top"></a>').prependTo('body');
    var $notes = $('<ol id="notes"></ol>').insertBefore('#footer');
    $('span.footnote').each(function(index) {
        $(this).before('<sup>+(index+1)+</sup>').appendTo($notes).wrap('<li></li>');
    });
});
