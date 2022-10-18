#!/usr/bin/node
const request = require('request');

const args = process.argv;
const a = args[2];

try {
  request
    .get(a)
    .on('error', (error) => {
      if (error) throw error;
    })
    .on('response', (response) => {
      console.log('code:', response.statusCode);
    });
} catch (error) {
  console.log(error);
}
