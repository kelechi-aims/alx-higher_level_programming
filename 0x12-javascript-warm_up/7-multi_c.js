#!/usr/bin/node
/*
 A script that prints x times “C is fun”
*/
const num = parseInt(process.argv[2]);
if (!isNaN(num) && num > 0) {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
