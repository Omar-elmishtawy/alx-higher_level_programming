#!/usr/bin/node

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    const film = JSON.parse(body);
    const chars_api = film.characters;
    const len_chars = chars_api.length;
    const list_char = [];
    console.log(chars_api[0]);
    for (let i = 0; i < len_chars; i++) {
      request(chars_api[i], function (error,response, body) {
        if (error) {
          console.log('error:', error);
        } else {
          console.log(JSON.parse(body).name);
	}
      });
    }
  }
});
