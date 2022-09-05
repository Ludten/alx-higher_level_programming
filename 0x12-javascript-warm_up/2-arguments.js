#!/usr/bin/node
const args = process.argv;
let out;
if (args.length <= 2) {
  out = 'No argument';
  console.log(out);
} else if (args.length === 3) {
  out = 'Argument found';
  console.log(out);
} else {
  out = 'Arguments found';
  console.log(out);
}
