$(document).ready(function() {
    var numberOfFaces = 5;
    var $theLeftSide = $('#leftside');
    var $theRightSide = $('#rightside');
    function generateFaces() {
        var i;
        var top_pos,left_pos;
        for (i = 0; i < numberOfFaces; i++) {
        	top_pos = Math.random()*400;
        	left_pos = Math.random()*400;
            $smile_img = $('<img>');
          	$smile_img.attr('src', '../images/smile.png');
          	$smile_img.css('top',top_pos+'px');
          	$smile_img.css('left',left_pos+'px');
          	$theLeftSide.append($smile_img);
        }
        var $leftSideImages = $theLeftSide.clone();
        $('img:last-child',$leftSideImages).remove();
        $theRightSide.append($leftSideImages);
    }
    (function initModule() {
    	generateFaces();

    })();

});
