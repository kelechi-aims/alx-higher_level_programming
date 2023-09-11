#!/usr/bin/node
/*
 A script that prints My number: <first argument converted in integer>
 if the first argument can be converted to an integer
*/
const arg = process.argv[2];
const num = parseInt(arg);

if (!isNaN(num)) {
  console.log('My number:', num);
} else {
  console.log('Not a number');
}
