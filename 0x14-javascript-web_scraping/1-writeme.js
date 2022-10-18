#!/usr/bin/node
const fs = require('fs');

const args = process.argv;
const a = args[2];
const b = args[3];

try {
  fs.writeFile(a, b, (err) => {
    if (err) throw err;
  });
} catch (error) {
  console.log(error);
}
