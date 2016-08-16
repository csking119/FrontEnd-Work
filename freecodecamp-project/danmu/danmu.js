var movement;

function danmu() {
    clearInterval(movement);
    var text = document.getElementById("text");
    var danmu = document.getElementById("danmu");
    //插入弹幕
    var textStyle = "<p id=\"textStyle\">" + text.value + "</p>";

    //设置弹幕的y轴坐标
    mathHeight = Math.round(Math.random() * danmu.offsetHeight) + "px";

    var textLeft = danmu.offsetWidth + "px";

    danmu.innerHTML = textStyle;

    var textStyleObj = document.getElementById("textStyle");

    textStyleObj.style.left = textLeft;
    textStyleObj.style.top = mathHeight;

    var x = parseInt(textStyleObj.style.left);

    //循环调用
    movement = setInterval("xunhuan(" + x + ")", 100);

}

function xunhuan(left) {
    var textStyleObj = document.getElementById("textStyle");
    textStyleObj.style.left = left;

    var x = parseInt(textStyleObj.style.left);
    
    //让弹幕重新回频幕右边
    if (x<0) {
        // document.getElementById("danmu").innerHTML = "";
        // clearInterval(movement);
        x=1200;
    } else {
        x -= 18;
    }
    //更新弹幕的坐标
    textStyleObj.style.left = x + "px";
}

//清屏
function clearDanmu() {
    if (document.getElementById("danmu").innerHTML) {
        document.getElementById("danmu").innerHTML = "";
        clearInterval(movement);
    }
}
