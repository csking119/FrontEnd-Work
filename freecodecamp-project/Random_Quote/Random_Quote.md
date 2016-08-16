# Random Quote

 这是一个随机获取名言的小程序，程序的Demo是下面这个样子：

![](http://oasnyeg67.bkt.clouddn.com/random_quote.JPG)

点击New quote按钮就可以随机获取一条quote。由于涉及到跨域，所以在接口里面使用了jsonp，然后在ajax里面定义了相应的jsonp毁掉函数。

接口地址url为：

https://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1&_jsonp=mycallback

其中filter为过滤条件，随机获取一条。

本程序的Codepen演示地址为：[Random Quote](https://codepen.io/athanzhang/pen/dXwVjO)







