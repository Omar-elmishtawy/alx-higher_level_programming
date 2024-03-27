#!/usr/bin/node

const url_path = process.argv[2];
const fs = require('fs');
const request = require('request');

request(url_path, function (error, response, body) {
  if (err) {
	  console.log(err);
  } else {
  	console.log('code: ',response.statusCode); // Print the response status code if a response was received
  }
});
