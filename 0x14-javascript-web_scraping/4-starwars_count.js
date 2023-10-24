#!/usr/bin/node

const args = process.argv;
const request = require('request');

const url = args[2].replace('films', 'people') + '/18';
request(url, (err, code, body) => {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.parse(body).films.length);
  }
});
