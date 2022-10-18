#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const args = process.argv;
const url = args[2];
const path = args[3];

try {
  request
    .get(url)
    .on('error', (error) => {
      if (error) throw error;
    })
    .pipe(fs.createWriteStream(path));
} catch (error) {
  console.log(error);
}
