#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
const dict = {};
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const obj = JSON.parse(body);
    let user = obj[0].userId;
    let TaskCount = 0;
    for (let a = 0; a < obj.length; a++) {
      if (obj[a].userId === user) {
        if (obj[a].completed === true) {
          TaskCount += 1;
        }
      } else {
        dict[user] = TaskCount;
        user = obj[a].userId;
        TaskCount = 0;
        if (obj[a].userId === user) {
          if (obj[a].completed === true) {
            TaskCount += 1;
          }
        }
      }
    }
    dict[user] = TaskCount;
  }
  console.log(dict);
});
