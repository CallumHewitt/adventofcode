const fs = require("fs");

// Input Parsing

const getInput = (inputFileNumber) => {
  return fs.readFileSync(getInputFileName(inputFileNumber), "utf-8");
};

const getInputFileName = (inputFileNumber) => {
  return "input" + inputFileNumber + ".txt";
};

const getInputList = (inputFileNumber) => {
  return getInput(inputFileNumber).split(/\r?\n/);
};

const getInputCharacters = (inputFileNumber, includeLineBreaks = false) => {
  return getInput(inputFileNumber)
    .split("")
    .filter((x) => x != "\n" && x != "\r");
};

const getInputListInts = (inputFileNumber) => {
  return getInputList(inputFileNumber).map((string) => parseInt(string, 10));
};

const getInput2DArray = (inputFileNumber, delimiter = "") => {
  return getInputList(inputFileNumber).map((s) => [...s.split(delimiter)]);
};

const ifNanThenZero = (number) => {
  return number ? number : 0;
};

// 2D Array Navigation

const findPosition = (twoDArray, x, y, xModifier, yModifier) => {
  const newX = x + xModifier;
  const newY = y + yModifier;
  if (newY < 0 || newY >= twoDArray.length) {
    return undefined;
  }
  if (newX < 0 || newX >= twoDArray[newY].length) {
    return undefined;
  }
  return {
    x: x + xModifier,
    y: y + yModifier,
    value: twoDArray[y + yModifier][x + xModifier],
  };
};

const findNorth = (twoDArray, x, y) => {
  return findPosition(twoDArray, x, y, 0, -1);
};

const findNorthEast = (twoDArray, x, y) => {
  return findPosition(twoDArray, x, y, 1, -1);
};

const findEast = (twoDArray, x, y) => {
  return findPosition(twoDArray, x, y, 1, 0);
};

const findSouthEast = (twoDArray, x, y) => {
  return findPosition(twoDArray, x, y, 1, 1);
};

const findSouth = (twoDArray, x, y) => {
  return findPosition(twoDArray, x, y, 0, 1);
};

const findSouthWest = (twoDArray, x, y) => {
  return findPosition(twoDArray, x, y, -1, 1);
};

const findWest = (twoDArray, x, y) => {
  return findPosition(twoDArray, x, y, -1, 0);
};

const findNorthWest = (twoDArray, x, y) => {
  return findPosition(twoDArray, x, y, -1, -1);
};

const findLocationsOfValue = (twoDArray, searchValue) => {
  let found = []
  for (let y = 0; y < twoDArray.length; y++) {
    for (let x = 0; x < twoDArray.length; x++) {
      if (twoDArray[y][x] == searchValue) {
        found.push({x, y, searchValue});
      }
    }
  }
  return found;
}

// GCD / LCM

const greatestCommonDivisor = (a, b) => {
  return b == 0 ? a : greatestCommonDivisor(b, a % b);
};

const lowestCommonMultiple = (a, b) => {
  return (a / greatestCommonDivisor(a, b)) * b;
};
const lowestCommonMultipleRange = (numbers) => {
  return numbers.reduce(lowestCommonMultiple, 1);
};

module.exports = {
  getInput,
  getInputCharacters,
  getInputList,
  getInputListInts,
  getInput2DArray,
  ifNanThenZero,
  findNorth,
  findNorthEast,
  findEast,
  findSouthEast,
  findSouth,
  findSouthWest,
  findWest,
  findNorthWest,
  findLocationsOfValue,
  greatestCommonDivisor,
  lowestCommonMultiple,
  lowestCommonMultipleRange,
};
