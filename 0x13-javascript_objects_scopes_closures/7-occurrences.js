#!/usr/bin/node

// returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let iter = 0;
  list.forEach(element => {
    if (searchElement === element) iter++;
  });
  return iter;
};
