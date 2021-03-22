#!/usr/bin/node
const argv = process.argv;
if (isNaN(argv[2])) {
  console.log(factorial(1, 1));
} else {
  console.log(factorial(parseInt(argv[2]), 1));
}
function factorial(a, sum) {
  if (a === 0){
    return sum
  }
  sum *= a;
  return factorial(a - 1, sum);
}
