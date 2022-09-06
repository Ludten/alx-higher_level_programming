#!/usr/bin/node
const fs = require('fs');

const args = process.argv;
const a = args[2];
const b = args[3];
const c = args[4];

try {
  const x = fs.readFileSync(a, 'utf8');

  const y = fs.readFileSync(b, 'utf8');

  const z = x + y;
  fs.writeFile(c, z, (err) => {
    if (err) throw err;
  });
} catch (err) {
  console.log(err);
}
