#!/usr/bin/node
const rp = require('request');

const args = process.argv;
const a = args[2];

try {
  rp('https://swapi-api.hbtn.io/api/films/' + a, async (error, response, body) => {
    if (error) throw error;
    const obj = JSON.parse(body);
    const res = obj.characters;
    for (let i = 0; i < res.length; i++) {
      await arrange(res[i]);
    }
  });
} catch (error) {
  console.log(error);
}

function arrange (url) {
  try {
    return new Promise(resolve => {
      setTimeout(function () {
        resolve(
          rp(url, (error, response, body) => {
            if (error) throw error;
            const char = JSON.parse(body);
            console.log(char.name);
          })
        );
      }, 1000);
    });
  } catch (error) {
    console.log(error);
  }
}
