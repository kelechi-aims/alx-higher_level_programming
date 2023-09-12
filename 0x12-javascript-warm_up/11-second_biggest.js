#!/usr/bin/node
/*
 A script that searches the second biggest integer in the list of arguments
*/
function findSecondLargest (args) {
  const numbers = args.map(Number);
  const integers = numbers.filter(number => Number.isInteger(number));
  const sortedIntegers = integers.sort((a, b) => b - a);
  if (sortedIntegers.length < 2) {
    return 0;
  }
  return sortedIntegers[1];
}
const args = process.argv.slice(2);
const result = findSecondLargest(args);
console.log(result);
