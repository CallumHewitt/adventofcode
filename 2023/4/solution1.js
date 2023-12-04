const tools = require("./tools");

const CARDS_REGEX = /Card\s*(\d*):\s*((\d*\s*)*)\|\s*((\d*\s*)*)/;

const solve1 = (input) => {
  return input
    .map((line) => parseCard(line))
    .reduce((acc, card) => acc + card.cardScore, 0);
};

const parseCard = (line) => {
  const cardMatch = line.match(CARDS_REGEX);
  const cardNumber = Number(cardMatch[1]);
  const targetNumbers = new Set(
    cardMatch[2]
      .split(/\s+/)
      .filter((x) => !!x)
      .map((x) => Number(x))
  );
  const entryNumbers = cardMatch[4]
    .split(/\s+/)
    .filter((x) => !!x)
    .map((x) => Number(x));
  const winningNumbers = entryNumbers.filter((n) => targetNumbers.has(n));
  const cardScore = winningNumbers.reduce((acc, c) => {
    if (acc == 0) {
      return 1;
    } else {
      return acc * 2;
    }
  }, 0);
  return {
    cardNumber,
    cardScore,
    targetNumbers,
    entryNumbers,
    winningNumbers,
  };
};

const solve2 = (input) => {
  const cardIndex = input.map((line) => parseCard(line));
  const toProcess = [...cardIndex];
  const processed = [];
  while (toProcess.length > 0) {
    const card = toProcess.pop();
    const wins = card.winningNumbers.length
    const newCards = cardIndex.slice(card.cardNumber, card.cardNumber + wins)
    toProcess.push.apply(toProcess, newCards);
    processed.push(card);
  }
  return processed.length
};

const input = tools.getInputList(1);
console.log("Q1: %s", solve1(input));
console.log("Q2: %s", solve2(input));
