#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    printMovieData(characters, 0);
  }
});

function printMovieData (characters, index) {
  request(characters[index], (charError, charResponse, charBody) => {
    if (charError) {
      console.error(charError);
    } else {
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
      if (index + 1 < characters.length) {
        printMovieData(characters, index + 1);
      }
    }
  });
}
