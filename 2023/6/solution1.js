const tools = require("./tools");

const solve1 = (input) => {
  const races = parseInput1(input);
  return races.map((race) => checkRace(race)).reduce((acc, c) => acc * c, 1);
};

const parseInput1 = (input) => {
  const times = input[0].split(/\s+/).slice(1);
  const records = input[1].split(/\s+/).slice(1);
  return times.map((t, i) => ({
    time: Number(t),
    record: Number(records[i]),
  }));
};

const checkRace = (race) => {
  let winCount = race.time
  for (let i = 1; i < race.time; i++) {
    const distance = i * (race.time - i);
    if (distance <= race.record) {
      winCount--
    }  else {
      break;
    }
  }
  for (let i = race.time; i > 0; i--) {
    const distance = i * (race.time - i);
    if (distance <= race.record) {
      winCount--
    }  else {
      break;
    }
  }
  return winCount;
};

const solve2 = (input) => {
  const race = parseInput2(input);
  return checkRace(race);
}

const parseInput2 = (input) => {
  const time = input[0].match(/Time:(.*)/)[1].replace(/\s/g, '')
  const record = input[1].match(/Distance:(.*)/)[1].replace(/\s/g, '')
  return {
    time: Number(time),
    record: Number(record),
  };
};

const input = tools.getInputList(1);
console.log("Q1:", solve1(input));
console.log("Q2:", solve2(input));
