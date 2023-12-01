const tools = require("./tools");

const solve1 = (input) => {
  return input
    .map((s) => s.replace(/[A-Za-z]/g, ""))
    .map((s) => Number(s[0] + s.slice(-1)))
    .reduce((acc, i) => acc + i, 0);
};

const solve2 = (input) => {
  return input.map(findFirstAndLast).reduce((acc, i) => acc + i, 0);
};

const findFirstAndLast = (s) => {
  let temp = s;
  const startingRegex =
    /^(one|two|three|four|five|six|seven|eight|nine|[0-9]).*/;
  while (!temp.match(startingRegex) && temp.length > 0) {
    temp = temp.slice(1);
  }
  const endingRegex = /(one|two|three|four|five|six|seven|eight|nine|[0-9])$/;
  while (!temp.match(endingRegex) && temp.length > 0) {
    temp = temp.slice(0, -1);
  }

  const start = temp.match(startingRegex)[1];
  const end = temp.match(endingRegex)[1];
  return Number(toDigit(start) + toDigit(end));
};

const toDigit = (s) => {
  switch (s) {
    case "one":
      return "1";
    case "two":
      return "2";
    case "three":
      return "3";
    case "four":
      return "4";
    case "five":
      return "5";
    case "six":
      return "6";
    case "seven":
      return "7";
    case "eight":
      return "8";
    case "nine":
      return "9";
    default:
      return s;
  }
};

const input = tools.getInputList(1);
console.log("Q1: %s", solve1(input));
console.log("Q2: %s", solve2(input));
