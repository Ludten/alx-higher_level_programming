#!/usr/bin/node
const rp = require('request-promise');

const args = process.argv;
const a = args[2];

async function order (res) {
  for (let i = 0; i < res.length; i++) {
    const options = {
      uri: res[i],
      json: true // Automatically parses the JSON string in the response
    };

    await rp(options)
      .then(function (repos) {
        console.log(repos.name);
      })
      .catch(function (err) {
        console.log(err);
      });
  }
}

try {
  rp('https://swapi-api.hbtn.io/api/films/' + a, (error, response, body) => {
    if (error) throw error;
    const obj = JSON.parse(body);
    const res = obj.characters;
    order(res);
  });
} catch (error) {
  console.log(error);
}
