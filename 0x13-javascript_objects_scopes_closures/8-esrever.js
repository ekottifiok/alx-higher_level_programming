#!/usr/bin/node

// returns the reversed version of a list
exports.esrever = function (list) {
  let listLen = list.length;
  if (listLen === 0) {
    return [];
  }
  const newArray = new Array(--listLen);
  list.forEach((element, index) => {
    newArray[listLen - index] = element;
  });
  return newArray;
};
