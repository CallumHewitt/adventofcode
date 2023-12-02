const tools = require("./tools");

const GAME_ID_REGEX = /Game (\d*): (.*)/;
const BLUE_REGEX = /(\d*) blue/;
const RED_REGEX = /(\d*) red/;
const GREEN_REGEX = /(\d*) green/;

const solve1 = (input) => {
  games = input.map(parseGame);
  return sumPossibleIds(12, 13, 14, games)
};

const parseGame = (line) => {
  const gameSplit = line.match(GAME_ID_REGEX);
  const gameId = gameSplit[1];
  const gameplay = gameSplit[2];
  const roundSplit = gameplay.split("; ");
  const rounds = [];
  let maxRed = 0;
  let maxGreen = 0;
  let maxBlue = 0;
  roundSplit.forEach((round) => {
    const redMatch = round.match(RED_REGEX);
    const greenMatch = round.match(GREEN_REGEX);
    const blueMatch = round.match(BLUE_REGEX);
    const roundResult = {};
    if (!!redMatch) {
      const red = Number(redMatch[1]);
      roundResult["red"] = red;
      if (red > maxRed) {
        maxRed = red;
      }
    }
    if (!!greenMatch) {
      const green = Number(greenMatch[1]);
      roundResult["green"] = green;
      if (green > maxGreen) {
        maxGreen = green;
      }
    }
    if (!!blueMatch) {
      const blue = Number(blueMatch[1]);
      roundResult["blue"] = blue;
      if (blue > maxBlue) {
        maxBlue = blue;
      }
    }
    rounds.push(roundResult);
  });
  return { gameId, maxRed, maxGreen, maxBlue, rounds };
};

const sumPossibleIds = (maxRed, maxGreen, maxBlue, games) => {
  let sum = 0;
  games.forEach(game => {
    if (game.maxRed <= maxRed &&
      game.maxGreen <= maxGreen &&
      game.maxBlue <= maxBlue) {
        sum += Number(game.gameId);
      }
  });
  return sum;
}

const solve2 = (input) => {
  games = input.map(parseGame);
  return calculateSumOfPowerSets(games)
};

const calculateSumOfPowerSets = (games) => {
  return games.map(game => game.maxRed * game.maxBlue * game.maxGreen).reduce((acc, c) => acc + c, 0)
}

const input = tools.getInputList(1);
console.log("Q1: %s", solve1(input));
console.log("Q2: %s", solve2(input));
