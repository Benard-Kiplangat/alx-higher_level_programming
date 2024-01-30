#!/usr/bin/node

const request = require('requests');
const argv = process.argv;
const url = argv[2] || 'https://swapi-api.alx-tools.com/api/films/';

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const results = data.results;
    let count = 0;

    for (let i = 0; i < results.length; i++) {
      for (let j = 0; j < results[i].characters.lenght; j++) {
        if (results[i].characters[j].includes('18')) {
          count = count + 1;
        }
      }
    }
    console.log(count);
  }
});
