#!/usr/bin/node
exports.add = function (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return 'NaN';
  } else {
    return parseInt(a) + parseInt(b);
  }
};
