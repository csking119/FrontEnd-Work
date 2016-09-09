$(document).ready(function() {
    var numberOfFaces = 2;
    var $theLeftSide = $('#leftside');
    var $theRightSide = $('#rightside');
    var $lastLeftChild;
    // generate faces
    function generateFaces() {
        var i;
        var top_pos, left_pos;
        for (i = 0; i < numberOfFaces; i++) {
            top_pos = Math.random() * 400;
            left_pos = Math.random() * 400;
            $smile_img = $('<img>');
            $smile_img.attr('src', '../images/smile.png');
            $smile_img.css('top', top_pos + 'px');
            $smile_img.css('left', left_pos + 'px');
            $theLeftSide.append($smile_img);
        }
        var $leftSideImages = $theLeftSide.clone();
        $('img:last-child', $leftSideImages).remove();
        $theRightSide.append($leftSideImages);

    }

    function deleteFaces() {
        $theLeftSide.empty();
        $theRightSide.empty();
    }

    function updateGame() {
        deleteFaces();
        generateFaces();
        $lastLeftChild = $('img:last-child', $theLeftSide);

        //rebind the click event to the new lastLeftChild
        $lastLeftChild.click(function(event) {
            event.stopPropagation();
            numberOfFaces += 1;
            updateGame();
        });
    }
    //initilization
    (function initModule() {
        generateFaces();
        $lastLeftChild = $('img:last-child', $theLeftSide);

    })();

    //update the lastchild of leftside

    $lastLeftChild.click(function(event) {
        event.stopPropagation();
        numberOfFaces += 1;
        updateGame();
    });

    $('body').click(function(event) {
    	alert("Game Over!");
    	$('body').off('click');
    	$lastLeftChild.off('click');

    });

});
