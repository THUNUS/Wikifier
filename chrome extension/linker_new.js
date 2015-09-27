// to implement the function to capture from the forum page and parse the content to hyper link with certain scheme
var docs="";
docs = $("div.course-forum-post-text");
var linked = docs;
var count=0;
var title = $("h1.course-topbanner-header a");
title = title.attr("href").replace(/[/]/g,'');
for(var i =0;i<linked.length;i++){
var content = linked[i].innerText;
var keyword = "(([Pp]roblem|[Qq]uizz*|[Qq]uestion|[Ee]xam|[Mm]odule|[Ll]ecture|[Ss]lide|[Vv]ideo|[Hh]omework|[Ww]eek)( *[0-9]+ *?[\.-]? *?[0-9]*)(?![0-9]*%))";

var reg = new RegExp(keyword); 
var patt = content.match(/(([Pp]roblem|[Qq]uizz*|[Qq]uestion|[Ee]xam|[Mm]odule|[Ll]ecture|[Ss]lide|[Vv]ideo|[Hh]omework|[Ww]eek)( *[0-9]+ *?[\.-]? *?[0-9]*)(?![0-9]*%))/g)
if (patt !=null){
	for(var j = 0;j<patt.length;j++){
		re = new RegExp(/(([Pp]roblem|[Qq]uizz*|[Qq]uestion|[Ee]xam|[Mm]odule|[Ll]ecture|[Ss]lide|[Vv]ideo|[Hh]omework|[Ww]eek)( *[0-9]+ *?[\.-]? *?[0-9]*))/i)
		result = re.exec(patt[j])
		if(result[3][0]==' '){
			result[3] = result[3].substring(1)
		}
		if(result[3][result.length-1]==','||result[3][result.length-1]=='.'){
			result[3] = result[3].substring(0,result.length-2);
		}
		linked[i].outerHTML=linked[i].outerHTML.replace(result[0],"<a href=\"http://127.0.0.1:8000\\resolve\\"+title+"\\"+result[2]+"\\"+result[3]+"\">"+result[0]+"</a>");
	}
	
	count++;
}

/**names = document.getElementsByName("name");
codes = document.getElementsByName("code");
for(var m = 0;m<names.length-1;m++){
	var patt = names[m].innerText.trim().split(" ");
	var str = "("
	for (var iter = 0; iter<patt.length;iter++){
		if(iter!=patt.length-1){
		str += patt[iter]+".{0,1}";
		}else
		{
		str +=patt[iter];
		}
	}
	str +=")"
	if(str!="(Classification)"&&str!="(Cost.{0,1}Function)"){
		var re = new RegExp(str,"ig")
	}else{
		var re = new RegExp(str,"g")
	}
	reg = content.match(re);
	if (reg !=null){
	for(var j = 0;j<reg.length;j++){
		result = reg[j];
		var re2 = new RegExp("(<a name.*>)(.*)(</a>)","g");
		var group = re2.exec(linked[i].outerHTML);
		if (group!=null&&result.match(group[2])){
		linked[i].outerHTML=linked[i].outerHTML.replace(group[0],group[2]);
		linked[i].outerHTML=linked[i].outerHTML.replace(result,"<a name = \"concret\" href=\"http://127.0.0.1:8000\\resolve\\"+coursename+"\\"+"lecture"+"\\"+names[m].innerText+"\">"+result+"</a>");
		}else
		{
			linked[i].outerHTML=linked[i].outerHTML.replace(result,"<a name = \"concret\" href=\"http://127.0.0.1:8000\\resolve\\"+coursename+"\\"+"lecture"+"\\"+names[m].innerText+"\">"+result+"</a>");
		}
	}
	
	count++;
}
	
}
**/
	
	}