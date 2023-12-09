const tools = require("./tools");

const solve1 = (input) => {
  const nextHistoryValues = findNextHistoryValues(input);
  return nextHistoryValues.reduce((acc, c) => acc + c, 0)
};

const findNextHistoryValues = (input) => {
  return input
    .map((l) => l.split(" ").map((i) => Number(i)))
    .map((line) => {
      const diffs = findDiffs(line);
      let newValue = 0;
      for (const diff of diffs) {
        newValue = diff.at(-1) + newValue;
      }
      return line.at(-1) + newValue;
    });
};

const findDiffs = (line) => {
  const diffs = [];
  let allSame = true;
  for (let i = 1; i < line.length; i++) {
    diffs.push(line[i] - line[i - 1]);
    if (i > 1 && diffs.at(-1) != diffs.at(-2)) {
      allSame = false;
    }
  }
  if (allSame) {
    return [diffs];
  } else {
    return [...findDiffs(diffs), diffs];
  }
};

const solve2 = (input) => {
  const previousHistoryValues = findPreviousHistoryValues(input);
  return previousHistoryValues.reduce((acc, c) => acc + c, 0)
};

const findPreviousHistoryValues = (input) => {
  return input
    .map((l) => l.split(" ").map((i) => Number(i)))
    .map((line) => {
      const diffs = findDiffs(line);
      let newValue = 0;
      for (const diff of diffs) {
        newValue = diff[0] - newValue;
      }
      return line[0] - newValue;
    });
};

const input = tools.getInputList(1);
console.log("==== Answers ====");
console.log("Q1:", solve1(input));
console.log("Q2:", solve2(input));
