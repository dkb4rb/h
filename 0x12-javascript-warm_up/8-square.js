#!/usr/bin/node
const { argv } = require('process');

if (isNaN(parseInt(argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  const count = parseInt(argv[2]);
  let c2 = count;
  while (c2 > 0) {
    console.log('X'.repeat(count));
    c2--;
  }
}
