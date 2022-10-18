#!/usr/bin/node
const request = require('request');

const args = process.argv;
const a = args[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + a;

try {
  request(url, (error, response, body) => {
    if (error) throw error;
    const obj = JSON.parse(body);
    console.log(obj.title);
});
} catch (error) {
  console.log(error);
}