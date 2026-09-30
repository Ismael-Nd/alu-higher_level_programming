#!/usr/bin/node
const occurrences = parseInt(process.argv[2]);

if (isNaN(occurrences)) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < occurrences; index++) {
    console.log('C is fun');
  }
}
