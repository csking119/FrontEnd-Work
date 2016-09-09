//define variables
var color = ["orange", "magenta", "gold", "green", "blue", "cyan", "red", "white", "yellow"];
var k; //to deposit the actual position of a color
var order_color = [];
var target,input;
var finished = false;

//order the colors
function sort_colors(color_array) {
    for (var i = 0; i < color_array.length - 1; i++) {
        k = 0;
        for (var j = 0; j < color_array.length; j++) {
            if (color_array[i] < color_array[j]) {
                if (j == color_array.length - 1) {
                    order_color[k] = color_array[i];
                }
                continue;
            } else if (color_array[i] > color_array[j]) {
                k++;
                if (j == color_array.length - 1) {
                    order_color[k] = color_array[i];
                }
            }

        }
    }
}
function check_guess(input) {
			for(var i=0;i<order_color.length;i++) {
				if(input!=order_color[i]) {
					continue;
				}
				else {
					break;
				}
				if (i==order_color.length) {
					alert("Sorry,I don't recognize your color \nPlease try again.");
					return;
				}
			}
			if(input>target){

				alert("Sorry,your guess is not correct! \nHint:your color is alphabetically higher than mine. \nPlease try again.")
			}
			else if(input<target) {
				alert("Sorry,your guess is not correct! \nHint:your color is alphabetically lower than mine. \nPlease try again.")
			}
			else if(input==target) {
				finished = true;
			}
		}

//main game function 
function do_game() {
	//get a random position
	var pos = parseInt(Math.random()*color.length);
	sort_colors(color);
	target = order_color[pos];
	var count = 0;		
	while(!finished) {
		input = prompt('I am thinking of one of these colors:\n '+order_color+'\nWhat color am i thinking of?')
		count++;
		check_guess(input);
	}
	document.body.style.background = target;
	alert("Congratuations! You have guessed the color! \n "+"It took you " + count +" guesses to finish the game! \nYou can see the color in the background.");
}
