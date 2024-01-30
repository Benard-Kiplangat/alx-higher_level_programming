#!/usr/bin/node

const request = require('request');
const argv = process.argv;
const rurl = argv[2];

request.get(rurl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const results = data.results;
    let count = 0;

    for (let i = 0; i < results.length; i++) {
      for (let j = 0; j < results[i].characters.length; j++) {
        if (results[i].characters[j].includes('18')) {
          count = count + 1;
        }
      }
    }
    console.log(count);
  }
});
