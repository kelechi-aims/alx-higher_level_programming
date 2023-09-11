#!/usr/bin/node
/*
 A script that prints the addition of 2 integers
*/
const a = process.argv[2];
const b = process.argv[3];

function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
add(a, b);
