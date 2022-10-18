#!/usr/bin/node
const request = require('request');

const args = process.argv;
const a = args[2];

try {
  request('https://swapi-api.hbtn.io/api/films/' + a, (error, response, body) => {
    if (error) throw error;
    const obj = JSON.parse(body);
    const res = obj.characters;
    for (let i = 0; i < res.length; i++) {
      request(res[i], (error, response, body) => {
        if (error) throw error;
        const char = JSON.parse(body);
        console.log(char.name);
      });
    }
  });
} catch (error) {
  console.log(error);
}
