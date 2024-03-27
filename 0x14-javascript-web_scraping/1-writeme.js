#!/usr/bin/node

const filePath = process.argv[2];
const fs = require('fs');
fs.writeFile(filePath, process.argv[3], function (err) {
  if (err) {
    console.log(err);
  }
});
