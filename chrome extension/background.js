// Copyright (c) 2011 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Called when the user clicks on the browser action.

chrome.browserAction.onClicked.addListener(function(tab) {
  // No tabs or host permissions needed!
	  chrome.tabs.executeScript(null,{
		file:"jquery.js"
	
  		});
	chrome.tabs.query({'active':true,'currentWindow':true},function(tabs){
	   var url = tabs[0].url;
	   var pattern_old = /class.*/igm;
		var pattern_new = /www.*/igm;
		if(pattern_old.exec(url)){
			console.log("this is old version!");
		   chrome.tabs.executeScript(null,{
			   
				file:"linker_old.js"
		  });
		   console.log("file loaded!");
		}else if(pattern_new.exec(url)){
			console.log("this is new version!");
			chrome.tabs.executeScript(null,{
				file:"linker_new.js"
			});
		}
		chrome.runtime.onMessage.addListener(function(request, sender, callback) {
    if (request.action == "xhttp") {
    	
        var xhttp = new XMLHttpRequest();
        var method = request.method ? request.method.toUpperCase() : 'GET';

        xhttp.onload = function() {
            callback(xhttp.responseText);
        };
        xhttp.onerror = function() {
            // Do whatever you want on error. Don't forget to invoke the
            // callback to clean up the communication port.
            callback();
        };
        var url = request.url+'/'+request.app+'/'+request.data+'/';
        xhttp.open(method, url, true);
        if (method == 'POST') {
            xhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        }
        xhttp.send(request.data);
        return true; // prevents the callback from being called too early on return
    }
});
	})
	
});
