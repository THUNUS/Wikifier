'use strict';	
// to implement the function to capture from the forum page and parse the content to hyper link with certain scheme
	var docs = $("div.course-forum-post-text");
	var post_title = $("h2");
	//loadCourseInfo("ml",course_info);
	if (docs.length!=0){
		
		var linked = docs;
		//linked.push.apply(linked,post_title);
		//alert(post_title.length);
		var count=0;
		var title = $("h1.course-topbanner-header a");
		title = title.attr("href").replace(/[/]/g,'');
		chrome.runtime.sendMessage({
		    method: 'GET',
		    action: 'xhttp',
		    url: 'http://127.0.0.1:8000',
		    app:'courseInfo',
		    data: title
		}, function(responseText) {
			var courseInfo = JSON.parse(responseText);
			//alert(courseInfo.course.length);
			for(var i =0;i<linked.length;i++){
		var content = linked[i].innerText;
		var reg = /((problem|quizz*|question|exam|module|lecture|slide|video|homework|week) *(\d+ *[-\.－] *\d+|\d+))/igm;
		var patt = content.match(reg);
		while ((result = reg.exec(content)) !== null) {
    		if (result.index === reg.lastIndex) {
        	reg.lastIndex++;
    		}
    		console.log(result);
				//alert(result);
				if(result[2].toLowerCase().trim().match("module|video")){
					result[2] = "lecture";
				}
				if(result[3].indexOf('-')>-1 || result[3].indexOf('.')>-1 || result[3].indexOf('—')>-1){
					if(result[3].indexOf('-')>-1){
						var subResult = result[3].split("-");
					}else if(result[3].indexOf('.')>-1){
						var subResult = result[3].split(".");
					}
					linked[i].innerHTML=linked[i].innerHTML.replace(result[0],"<a style=\"color:green\" href=\"http://127.0.0.1:8000\\resolve\\"+title+"\\"+result[2].toLowerCase().trim()+"\\"+subResult[0].trim()+"\\section\\"+subResult[1].trim()+"\">"+result[0].trim()+"</a>");
				}else{
					linked[i].innerHTML=linked[i].innerHTML.replace(result[0],"<a style=\"color:green\" href=\"http://127.0.0.1:8000\\resolve\\"+title+"\\"+result[2].toLowerCase().trim()+"\\"+result[3].trim()+"\">"+result[0].trim()+"</a>");
				}
				
			
			
			count++;
		}

		var videos = courseInfo.course;
		for(var m = videos.length-1;m>=0;m--){
			//console.log(videos[m].video);
			var patt = videos[m].video.split(" ");
			if ( patt.length>1 ){
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
				var result = reg[j];
				var re2 = new RegExp("(<a style.*>)(.*)(</a>)","g");
				var group = re2.exec(linked[i].innerHTML);
				if (group!=null&&result.match(group[2])){
				linked[i].innerHTML=linked[i].innerHTML.replace(group[0],group[2]);
				linked[i].innerHTML=linked[i].innerHTML.replace(result,"<a style = \"color: green\" name = \"concret\" href=\"http://127.0.0.1:8000\\resolve\\"+title+"\\"+"lecture"+"\\"+videos[m].video+"\">"+result+"</a>");
				}else
				{
					linked[i].innerHTML=linked[i].innerHTML.replace(result,"<a style = \"color: green\" name = \"concret\" href=\"http://127.0.0.1:8000\\resolve\\"+title+"\\"+"lecture"+"\\"+videos[m].video+"\">"+result+"</a>");
				}
			}
			
			count++;
			}
		}	
			}
		
	}

	for(var i =0;i<linked.length;i++){
				var a = $(linked[i]).find("a");
				//alert(a.length);
				if(a.length>=2){
					for(var a_iter = 0;a_iter<a.length;a_iter++){
						if(String(a[a_iter].innerHTML).match(/(slide)|(question)/ig)){
							for(var new_iter = 0;new_iter<a.length;new_iter++){
								if(String(a[new_iter].innerHTML).match(/(lecture)|(quiz[z]*)|(week)|(assignment)|(video)|(module)/ig)){
									if(new_iter>a_iter){
										var content = String(linked[i].innerHTML);
										var child = String(a[a_iter].outerHTML);
										var parent = String(a[new_iter].outerHTML);
										//alert(parent);
										var reg3 = /[0-9]+/igm;
										var index = content.substring(content.indexOf(child),content.indexOf(parent)+parent.length);
										//alert(index);
										//alert(content.indexOf(index));
										linked[i].innerHTML = content.replace(index,"<a style = \"color: green\" cls = \"inherit\" parent = \"lecture\" child = \"slide\" href = \"http://127.0.0.1:8000\\resolve\\"+title+"\\"+a[new_iter].innerHTML.split(" ")[0].toLowerCase()+"\\"+String(a[new_iter].innerHTML).match(reg3)[0] + "\\"+a[a_iter].innerHTML.split(" ")[0].toLowerCase()+"\\"+String(a[a_iter].innerHTML).match(reg3)[0]+"\">"+a[a_iter].innerHTML+" of "+a[new_iter].innerHTML+"</a>");
							
										;
										;
									}
								}

							}
						}
					}
				}
				//wikify term
				if(linked[i].innerHTML.match(/log-normal/i)){
					reg = linked[i].innerHTML.match(/log-normal/i);
					//alert(reg);
					linked[i].innerHTML = linked[i].innerHTML.replace(reg,"<a style = \"color:green\" bubbletooltip = \"Hi I am a bubble tooltip\" cls = \"wikipedia\" href = \"https://en.wikipedia.org/wiki/Log-normal_distribution\"> "+reg+"</a>");
					
				}

			}


	
	alert("There are "+count+" items have been wikified!");
		});
		
		}


