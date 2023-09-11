#!/usr/bin/node

/*
 A script that prints the first argument passed to it
*/
if (process.argv[2] === undefined) {
  console.log('No arguments');
} else {
  console.log(process.argv[2]);
}
