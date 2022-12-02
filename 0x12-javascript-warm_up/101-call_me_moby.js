#!/usr/bin/node

exports.callMeMoby = function (x, func) {
  for (let index = 0; index < x; index++) {
    func();
  }
};
