#!/usr/bin/node
let basenum = 0;

exports.converter = function converter (base) {
  if (basenum === 0) {
    console.log(basenum);
    basenum = base;
    console.log(basenum);
    return (converter);
  } else {
    let num = base;
    let numConvert = '';
    for (; parseInt(num / basenum) > 0;) {
      numConvert = numConvert + (num % basenum);
      num = parseInt(num / basenum);
    }
    console.log(numConvert);
    return (numConvert);
  }
};
