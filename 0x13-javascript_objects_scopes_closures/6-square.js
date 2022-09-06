#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        let disp = '';
        for (let j = 0; j < this.width; j++) {
          disp += 'c';
        }
        console.log(disp);
      }
    } else {
      this.print();
    }
  }
};
