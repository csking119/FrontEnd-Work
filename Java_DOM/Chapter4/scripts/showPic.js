function showPic(whichPic) {
	var source = whichPic.getAttribute("href");
	var placeholder=document.getElementById("placeholder");
	placeholder.setAttribute("src",source);
	//获取节点title值
	var title = whichPic.getAttribute("title");
	//获取相应ID对象
	var description= document.getElementById("description");
	//替换相应对象值
	description.firstChild.nodeValue=title;
}