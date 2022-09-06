#!/usr/bin/node
const dict = require('./101-data').dict;

const ret = {};
for (const key in dict) {
  if (ret[dict[key]] !== undefined) {
    ret[dict[key]].push(key);
  } else {
    ret[dict[key]] = [];
    ret[dict[key]].push(key);
  }
}
console.log(ret);
