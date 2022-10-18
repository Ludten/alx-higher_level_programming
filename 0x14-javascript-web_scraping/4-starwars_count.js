#!/usr/bin/node
const request = require('request');

const args = process.argv;
const url = args[2];
let ctr = 0;

try {
  request(url, (error, response, body) => {
    if (error) throw error;
    const obj = JSON.parse(body);
    const res = obj.results;
    for (let i = 0; i < res.length; i++) {
      for (let j = 0; j < res[i]['characters'].length; j++) {
        if ( res[i]['characters'][j].includes('people/18')) {
          ctr++;
        }
      }
    }
    console.log(ctr);
});
} catch (error) {
  console.log(error);
}
