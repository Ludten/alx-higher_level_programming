#!/usr/bin/node
const square = require('./5-square');

module.exports = class Square extends square {
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        let disp = '';
        for (let j = 0; j < this.width; j++) {
          disp += c;
        }
        console.log(disp);
      }
    } else {
      this.print();
    }
  }
};
