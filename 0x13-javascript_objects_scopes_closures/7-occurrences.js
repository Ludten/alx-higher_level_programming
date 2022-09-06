#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let ctr = 0;

  for (const elem of list) {
    if (searchElement === elem) {
      ctr++;
    }
  }
  return ctr;
};
