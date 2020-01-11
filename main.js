function getUrl(url){
	var target;
	var result;
	target = "userName : " + url;
	target = url.replace(/\/|\=|\:|\s/gi,"");
	return target;
}
var id = getUrl("SonarCloud!");
