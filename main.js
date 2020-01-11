function getUrl(url){
	var target;
	var result;
	target = "userName : " + url;
	target = url.replace(/\/|\=|\:|\s/gi,"");
	 window.alert(target) 
}
getUrl("SonarCloud!");
