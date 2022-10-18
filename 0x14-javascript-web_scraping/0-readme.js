#!/usr/bin/node
const fs = require('fs');

const args = process.argv;
const a = args[2];

try {
  const x = fs.readFileSync(a, 'utf8');
  console.log(x);
} catch (error) {
  console.log(error);
}
