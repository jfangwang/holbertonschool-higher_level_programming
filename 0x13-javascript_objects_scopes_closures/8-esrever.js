#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length;
  if (len % 2 !== 0) {
    len += 1;
  }
  let temp = 0;
  for (let a = 0; a < (len / 2); a++) {
    temp = list[a];
    list[a] = list[list.length - a - 1];
    list[list.length - a - 1] = temp;
  }
  return list;
};
