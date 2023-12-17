const tools = require("./tools");

const solve1 = (input) => {
  const springRecords = parseInput(input);
  const validConfigurations = springRecords.map(findValidConfigurations);
  return validConfigurations.map(c => c.length).reduce((acc, c) => acc + c, 0)
};

const parseInput = (input) => {
  return input.map((line) => {
    const splitLine = line.split(" ");
    const row = splitLine[0].split("");
    const checkCounts = splitLine[1].split(",").map(Number);
    const questionIndexes = row.map((x, i) => (x == "?" ? i : -1)).filter((x) => x != -1);
    return {
      row,
      checkCounts,
      questionCount: questionIndexes.length,
      questionIndexes,
      expectedSpringCount: checkCounts.reduce((acc, c) => acc + c, 0),
      currentSpringCount: row.filter((x) => x == "#").length,
      checkRegex: createCheckRegex(checkCounts),
    };
  });
};

const createCheckRegex = (checkCounts) => {
  return new RegExp("^\\.*" + checkCounts.map((count) => "#{" + count + "}").join("\\.+") + "\\.*$");
};

const findValidConfigurations = (record) => {
    const magnitude = record.questionCount;
    const springsToAdd = record.expectedSpringCount - record.currentSpringCount;
    const binaries = tools.range(Math.pow(2, magnitude))
        .map(n => Number(n).toString(2).padStart(magnitude, '0').split(''))
        .filter(s => s.reduce((acc, c) => c == '1' ? acc + 1 : acc, 0) == springsToAdd)
        .map(x => x.map(y => y == '0' ? '.' : '#'))
    const matches = []
    binaries.forEach(binary => {
        const newRow = record.row;
        record.questionIndexes.forEach((questionIndex, binaryIndex) => {
            newRow[questionIndex] = binary[binaryIndex]
        });
        const newRowString = newRow.join('')
        if (newRowString.match(record.checkRegex)) {
            matches.push(newRowString)
        }
    });
    return matches;
};

const solve2 = (input) => {
    const springRecords = parseFoldedInput(input);
    const validConfigurations = springRecords.map(findValidConfigurations);
    return validConfigurations.map(c => c.length).reduce((acc, c) => acc + c, 0)
};

const parseFoldedInput = (input) => {
    return input.map((line) => {
      const splitLine = line.split(" ");
      const row = tools.range(0, 5).map(_ => splitLine[0]).join('?').split("");
      const checkCounts = tools.range(0, 5).map(_ => splitLine[1]).join(',').split(",").map(Number);
      const questionIndexes = row.map((x, i) => (x == "?" ? i : -1)).filter((x) => x != -1);
      return {
        row,
        checkCounts,
        questionCount: questionIndexes.length,
        questionIndexes,
        expectedSpringCount: checkCounts.reduce((acc, c) => acc + c, 0),
        currentSpringCount: row.filter((x) => x == "#").length,
        checkRegex: createCheckRegex(checkCounts),
      };
    });
  };

const input = tools.getInputList(0);
console.log("==== Answers ====");
console.log("Q1:", solve1(input));
console.log("Q2:", solve2(input));