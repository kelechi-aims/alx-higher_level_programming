#!/usr/bin/node
/*
 A function that executes x times a function
*/
exports.callMeMoby = function (x, theFunc) {
  for (let i = 0; i < x; i++) {
    theFunc();
  }
};
