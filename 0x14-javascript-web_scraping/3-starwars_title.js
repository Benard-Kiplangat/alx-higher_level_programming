#!/usr/bin/node

const request = require('request');
const args = process.argv;
const requestURL = 'https://swapi-api.hbtn.io/api/films/' + args[2];

request.get(requestURL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
