#!/usr/bin/node

exports.converter = function (base) {
  function newbase (params) {
    return (params.toString(base));
  }
  return newbase;
};
