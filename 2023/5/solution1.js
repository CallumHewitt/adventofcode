const tools = require("./tools");

// PARSING
const parseAlmanac = (input) => {
  const seeds = parseSeeds(input);
  const maps = parseMaps(input);
  const mapByFrom = maps.reduce((acc, map) => ({ ...acc, [map.from]: map }), {});
  const mapByTo = maps.reduce((acc, map) => ({ ...acc, [map.to]: map }), {});
  return {
    seeds,
    maps,
    mapByFrom,
    mapByTo,
  };
};

const parseSeeds = (input) => {
  return input[0]
    .match(/seeds: (.*)/)[1]
    .split(" ")
    .map((x) => Number(x));
};

const parseMaps = (input) => {
  const mapNameRegex = /([a-z]*)-to-([a-z]*) map:/;
  const numbersRegex = /([0-9]*) ([0-9]*) ([0-9]*)/;
  const maps = [];
  input
    .slice(1)
    .filter((x) => !!x)
    .forEach((line) => {
      const mapNameMatch = line.match(mapNameRegex);
      if (!!mapNameMatch) {
        maps.push({
          from: mapNameMatch[1],
          to: mapNameMatch[2],
          targetingParameters: [],
        });
      } else {
        const numbersMatch = line.match(numbersRegex);
        const destinationRangeStart = Number(numbersMatch[1]);
        const sourceRangeStart = Number(numbersMatch[2]);
        const range = Number(numbersMatch[3]);
        maps.at(-1).targetingParameters.push({
          destinationRangeStart,
          sourceRangeStart,
          range,
        });
      }
    });
  return maps;
};

// QUESTION 1
const findClosestLocation = (almanac) => {
  const traced = almanac.seeds.map((seed) => {
    return traceThroughAlmanac("seed", "location", almanac, seed);
  });
  return Math.min.apply(Math, traced.flat());
};

const traceThroughAlmanac = (startCategory, targetCategory, almanac, startValue) => {
  const map = almanac.mapByFrom[startCategory];
  const value = findDestination(startValue, map.targetingParameters);
  if (map.to === targetCategory) {
    return value;
  } else {
    return traceThroughAlmanac(map.to, targetCategory, almanac, value);
  }
};

const findDestination = (source, targetingParameters) => {
  for (let parameters of targetingParameters) {
    const sourceRangeStart = parameters.sourceRangeStart;
    const range = parameters.range;
    if (source >= sourceRangeStart && source < sourceRangeStart + range) {
      return parameters.destinationRangeStart + source - sourceRangeStart;
    }
  }
  return source;
};

// QUESTION 2
const findClosestLocationAsSeedRanges = (almanac) => {
  const seedRanges = [];
  for (let i = 0; i < almanac.seeds.length; i += 2) {
    seedRanges.push([almanac.seeds[i], almanac.seeds[i] + almanac.seeds[i + 1]]);
  }
  const maxLocation = Math.max.apply(
    Math,
    almanac.mapByTo["location"].targetingParameters.map((p) => p.destinationRangeStart + p.range)
  );
  for (let location = 1; location <= maxLocation; location++) {
    const seed = backTraceAlmanac("location", "seed", almanac, location);
    if (seedRanges.some((r) => seed >= r[0] && seed <= r[1])) {
      return location;
    }
  }
};

const backTraceAlmanac = (startCategory, targetCategory, almanac, startValue) => {
  const map = almanac.mapByTo[startCategory];
  const value = findSource(startValue, map.targetingParameters);
  if (map.from === targetCategory) {
    return value;
  } else {
    return backTraceAlmanac(map.from, targetCategory, almanac, value);
  }
};

const findSource = (destination, targetingParameters) => {
  for (let parameters of targetingParameters) {
    const destinationRangeStart = parameters.destinationRangeStart;
    const range = parameters.range;
    if (destination >= destinationRangeStart && destination < destinationRangeStart + range) {
      return parameters.sourceRangeStart + destination - destinationRangeStart;
    }
  }
  return destination;
};

const input = tools.getInputList(1);
const almanac = parseAlmanac(input);
console.log("Q1:", findClosestLocation(almanac));
console.log("Q2:", findClosestLocationAsSeedRanges(almanac));