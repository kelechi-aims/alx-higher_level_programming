#!/usr/bin/node
/*
 A script that computes and prints a factorial
*/
function factorial (n) {
  if (isNaN(n) || n < 2) {
    return 1;
  }
  return n * factorial(n - 1);
}
console.log(factorial(parseInt(process.argv[2])));
