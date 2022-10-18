#!/usr/bin/node
const request = require('request');

const args = process.argv;
const url = args[2];
const pdict = {};

try {
  request(url, (error, response, body) => {
    if (error) throw error;
    const obj = JSON.parse(body);
    let ctr = 0;
    for (let i = 0; i < obj.length; i++) {
      if (obj[i].completed === true) {
        if (obj[i].userId in pdict) {
          pdict[obj[i].userId] = ++ctr;
        } else {
          ctr = 0;
          pdict[obj[i].userId] = ++ctr;
        }
      }
    }
    console.log(JSON.parse(JSON.stringify(pdict)));
  });
} catch (error) {
  console.log(error);
}
