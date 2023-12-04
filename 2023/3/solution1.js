const tools = require("./tools");

const SYMBOLS = new Set(
  tools.getInputCharacters(1).filter((x) => !x.match(/[0-9\.]/))
);

const solve1 = (input) => {
  const parts = extractParts(input);
  return parts.map((p) => p.partNumber).reduce((acc, c) => acc + c, 0);
};

const extractParts = (input) => {
  let parts = [];
  input.forEach((line, y) => {
    let numberAcc = "";
    line.forEach((character, x) => {
      const characterIsNumber = isNumber(character);
      if (characterIsNumber) {
        numberAcc += character;
      }
      if ((!characterIsNumber && numberAcc != "") || x == line.length - 1) {
        const part = checkPartDetails(input, x, y, numberAcc);
        if (part.adjacentSymbols.length != 0) {
          parts.push(part);
        }
        numberAcc = "";
      }
    });
  });
  return parts;
};

const isNumber = (s) => {
  return s.match(/[0-9]/);
};

const checkPartDetails = (input, endX, y, partNumber) => {
  const startX = endX - partNumber.length;
  adjacents = [];
  for (let i = 0; i < partNumber.length; i++) {
    if (input[y - 1] != undefined) {
      adjacents.push(createSymbolRecord(input, startX + 1 + i, y - 1));
      adjacents.push(createSymbolRecord(input, startX + i, y - 1));
      adjacents.push(createSymbolRecord(input, startX - 1 + i, y - 1));
    }
    if (input[y] != undefined) {
      adjacents.push(createSymbolRecord(input, startX + 1 + i, y));
      adjacents.push(createSymbolRecord(input, startX - 1 + i, y));
    }
    if (input[y + 1] != undefined) {
      adjacents.push(createSymbolRecord(input, startX + 1 + i, y + 1));
      adjacents.push(createSymbolRecord(input, startX + i, y + 1));
      adjacents.push(createSymbolRecord(input, startX - 1 + i, y + 1));
    }
  }
  const adjacentSymbols = adjacents
    .filter((x) => !!x.symbol)
    .filter((x) => SYMBOLS.has(x.symbol))
    .filter(
      (value, index, self) =>
        index === self.findIndex((t) => t.x === value.x && t.y === value.y)
    );
  return {
    partNumber: Number(partNumber),
    startX,
    endX,
    y,
    adjacentSymbols,
  };
};

const createSymbolRecord = (input, x, y) => {
  return {
    x,
    y,
    symbol: input[y][x],
  };
};

const solve2 = (input) => {
  const parts = extractParts(input);
  const gears = parts
    .map((part) => part.adjacentSymbols)
    .flat()
    .filter((s) => s.symbol == "*")
    .filter(
      (value, index, self) =>
        index === self.findIndex((t) => t.x === value.x && t.y === value.y)
    );
  const partsByGear = gears.map((gear) => [
    gear,
    parts.filter(
      (part) =>
        part.adjacentSymbols.filter(
          (s) => s.symbol == "*" && s.x == gear.x && s.y == gear.y
        ).length != 0
    ),
  ]);
  const gearRatioSum = partsByGear.reduce((acc, pair) => {
    const parts = pair[1];
    console.log(parts);
    if (parts.length == 2) {
      return acc + (parts[0].partNumber * parts[1].partNumber);
    }
    return acc;
  }, 0);
  return gearRatioSum;
};

const input = tools.getInput2DArray(1);
console.log(SYMBOLS);
console.log("Q1: %s", solve1(input));
console.log("Q2: %s", solve2(input));
