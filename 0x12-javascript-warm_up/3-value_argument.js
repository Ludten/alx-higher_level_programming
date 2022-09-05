#!/usr/bin/node
const args = process.argv;
let out;

if (args[2] === undefined) {
  out = 'No argument';
  console.log(out);
} else {
  out = args[2];
  console.log(out);
}
