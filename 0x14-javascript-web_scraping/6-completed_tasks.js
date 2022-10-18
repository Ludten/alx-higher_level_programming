#!/usr/bin/node
const request = require('request');

const args = process.argv;
const url = args[2];

try {
  request(url, (error, response, body) => {
    if (error) throw error;
    const obj = JSON.parse(body);
    const filtered = obj.filter(a => a.completed === true);
    const pdict = {};
    for (let i = 0; i < filtered.length; i++) {
      if (filtered[i].userId in pdict) {
        pdict[filtered[i].userId] += 1;
      } else {
        pdict[filtered[i].userId] = 1;
      }
    }
    console.log(pdict);
  });
} catch (error) {
  console.log(error);
}
