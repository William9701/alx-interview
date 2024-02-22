#!/usr/bin/node
const req = require("request");
const parameters = process.argv;

const retrieveCharacter = (url) => {
  return new Promise((resolve, reject) => {
    req(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const char = JSON.parse(body);
        resolve(char.name);
      } else {
        reject(error);
      }
    });
  });
};

if (parameters.length === 3) {
  req(
    `https://swapi-api.alx-tools.com/api/films/${parameters[2]}`,
    (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const chars = JSON.parse(body).characters;

        const retrievePromises = chars.map((url) => retrieveCharacter(url));
        Promise.all(retrievePromises)
          .then((names) => {
            names.forEach((name) => console.log(name));
          })
          .catch((error) => console.error("Error:", error));
      } else {
        console.error("Error:", error);
      }
    }
  );
}
