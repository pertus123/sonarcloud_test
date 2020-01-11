function Nulltest (check) {
	var marks match;
	var html;

	if(!check){
		;(function(window, document){
			var html = {};
		window.html = html;
	}(typeof window !== 'undefined' ? window : this	, document));
	}

	if(marks.length > 1){
		match = marks[marks.length - 2];
	}else{
		match = null;
	}

	return match.mark, html;
};// 초기화되지 않은 변수 사용
Nulltest(1);
