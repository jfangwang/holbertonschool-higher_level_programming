const Rectangle = require('./5-square');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let a = 0; a < this.height; a++) {
      for (let b = 0; b < this.width; b++) {
        process.stdout.write(c);
      }
      console.log('');
    }
  }
};
