#!/usr/bin/node
const args = process.argv;
const out = parseInt(args[2]);
if (isNaN(out)) {
  console.log('Missing number of occurrences');
} else {
  if (out > 0) {
    for (let i = 0; i < out; i++) {
      console.log('C is fun');
    }
  }
}
