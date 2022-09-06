#!/usr/bin/node

let calledTimes = 0;
exports.logMe = function (item) {
  console.log(`${calledTimes}: ${item}`);
  calledTimes++;
};
