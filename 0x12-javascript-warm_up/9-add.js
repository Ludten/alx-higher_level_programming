#!/usr/bin/node
const args = process.argv;
const out1 = parseInt(args[2]);
const out2 = parseInt(args[3]);
if (isNaN(out1) || isNaN(out2)) {
  console.log(NaN);
} else {
  const sum = out1 + out2;
  console.log(sum);
}
