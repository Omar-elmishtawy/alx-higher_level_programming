#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const api = process.argv[2];
const filepath = process.argv[3];

request({ url: api, methods: 'GET' }, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filepath, body, function (err) {
	    if (err) {
		    console.log(err);
	    }
  }
});
});
