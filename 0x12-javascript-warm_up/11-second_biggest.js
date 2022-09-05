#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  const data = [];
  for (let i = 2; i < args.length; i++) {
    data.push(parseInt(args[i]));
  }
  data.sort(function (a, b) { return a - b; });
  console.log(data[data.length - 2]);
}
