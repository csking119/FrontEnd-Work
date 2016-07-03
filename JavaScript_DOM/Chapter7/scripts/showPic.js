
//HTML加载完成时启动函数win.onload：这里判断win.load是否有绑定处理函数，
//如果有，添加新的到后面，如果没有，直接添加
function addLoadEvent(func) {
    var oldonload = window.onload;
    if (typeof window.onload != 'function') {
        window.onload = func;
    }
    else {
        window.onload = function() {
            oldonload();
            func();
        }
    }

}

//在相应节点后插入新节点
function insertAfter(newElement,targetElment) {
    var parent= targetElment.parentNode;
    if(parent.lastChild==targetElment) {
        parent.appendChild(newElement);
    }
    else {
        parent.insertBefore(newElement,targetElment.nextSibling);
    }
}

//创建节点placeholder、description
function preparePlaceholder() {
    if (!document.createElement) return false;
    if (!document.createTextNode) return false;
    if (!document.getElementById) return false;
    if (!document.getElementById("imagegallery")) return false;
    var placeholder=document.createElement("img");
    placeholder.setAttribute("id","placeholder");
    placeholder.setAttribute("src","./images/yun.jpg");
    placeholder.setAttribute("alt","my image gallery");
    var description=document.createElement("p");
    description.setAttribute("id","description");
    var desctext=document.createTextNode("Choose an image");
    description.appendChild(desctext);
    var gallery = document.getElementById("imagegallery");
    insertAfter(placeholder,gallery);
    insertAfter(description,placeholder);
}

function showPic(whichPic) {
    //如果placeholder不存在，保证跳转正常
    if (!document.getElementById("placeholder")) return true;
    var source = whichPic.getAttribute("href");
    var placeholder = document.getElementById("placeholder");
    placeholder.setAttribute("src", source);
    //如果description不存在，不执行
    if (!document.getElementById("description")) return false;
    //获取节点title值
    var text = whichPic.getAttribute("title");
    //获取相应ID对象
    var description = document.getElementById("description");
    //替换相应对象值
    description.firstChild.nodeValue = text;
    //图片和文字都替换，保证click不执行默认动作
    return false;
}

function prepareGallery() {
    if (!document.getElementsByTagName) return false;
    if (!document.getElementById) return false;
    if (!document.getElementById("imagegallery")) return false;
    var gallery = document.getElementById("imagegallery");
    var links = gallery.getElementsByTagName("a");
    for (var i = 0; i < links.length; i++) {
        links[i].onclick = function() {
            return showPic(this);

        }
    }
}




addLoadEvent(preparePlaceholder);
addLoadEvent(prepareGallery);

