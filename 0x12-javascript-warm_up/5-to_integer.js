#!/usr/bin/node
const { argv } = require('process');
const converint = parseInt(argv[2]);
if (converint) { console.log('My number: ' + converint); } else { console.log('Not a Number'); }
