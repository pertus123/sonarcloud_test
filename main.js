function getUrl(url){
	var target;
	var result;
	target = url + "userName" + userName;
	target = url.replace(/\/|\=|\:|\s/gi,"");
	return target;
}
getUrl();
