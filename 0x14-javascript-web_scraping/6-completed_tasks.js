#!/usr/bin/node

const args = process.argv;
const request = require('request');

request(args[2], (err, code, body) => {
  if (err) { console.error(err); } else {
    const users = {};
    for (let i = 1; i <= 10; i++) {
      users[i] = JSON.parse(body).filter(task => task.completed && task.userId === i).length;
    }
    console.log(users);
  }
});
