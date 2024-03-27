#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const parsedBody = JSON.parse(body);
    const dict = {};
    let count = 0;
    let userId = parsedBody[0].userId;
    for (let i = 0; i < parsedBody.length; i++) {
      if (userId === parsedBody[i].userId && parsedBody[i].completed) {
        count = count + 1;
      } else if (userId !== parsedBody[i].userId) {
        dict[userId] = count;
        userId = parsedBody[i].userId;
        count = 0;
        i = i - 1;
      } else {
        return;
      }
    }
    dict[userId] = count;
    console.log(dict);
  }
});
