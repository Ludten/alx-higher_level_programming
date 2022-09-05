#!/usr/bin/node
const args = process.argv;
const out = parseInt(args[2]);
if (isNaN(out)) {
  console.log('Missing size');
} else {
  if (out > 0) {
    for (let i = 0; i < out; i++) {
      let disp = '';
      for (let j = 0; j < out; j++) {
        disp += 'X';
      }
      console.log(disp);
    }
  }
}
