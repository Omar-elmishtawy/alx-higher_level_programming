#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
	  const parsedBody = JSON.parse(body);
	  const dict = {};
	  var count = 0;
	  var user_id = parsedBody[0].userId;
	  for (let i = 0; i < parsedBody.length; i++){
	     if (user_id === parsedBody[i].userId && parsedBody[i].completed) {
		     count = count + 1;
	     } else if (user_id !== parsedBody[i].userId){
		     dict[user_id] = count;
		     user_id = parsedBody[i].userId;
		     count = 0;
		     i = i - 1;
	     }
	  }
	  dict[user_id] = count;
	  console.log(dict);
  }
});
	    
