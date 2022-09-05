#!/usr/bin/node
const args = process.argv;
const out = parseInt(args[2]);
if (isNaN(out)) {
  console.log(1);
} else {
  const fact = factorial(out);
  console.log(fact);
}

function factorial (num) {
  if (num === 1) return 1;
  if (num === 0) return 1;

  return num * factorial(num - 1);
}
