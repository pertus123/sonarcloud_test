function getUrl(url){
	var target;
	var result;
	target = "userName : " + url;
	target = url.replace(/\/|\=|\:|\s/gi,"");
	return target;
}
getUrl("SonarCloud!");
