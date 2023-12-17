const tools = require("./tools");

const solve = (map) => {
  const navChart = createNavigationChart(map);
  const galaxyPairs = pairGalaxies(navChart.galaxyPositions);
  const twoRatioDistances = calculateDistances(galaxyPairs, 2, navChart);
  const millionRatioDistances = calculateDistances(galaxyPairs, 1_000_000, navChart);
  console.log("Q1:", twoRatioDistances.reduce((acc, c) => acc + c, 0));
  console.log("Q2:", millionRatioDistances.reduce((acc, c) => acc + c, 0));
}

const createNavigationChart = (map) => {
  return {
    map,
    galaxyPositions: tools.findLocationsOfValue(map, '#'),
    emptyY: map.map((row, i) => row.every(p => p == '.') ? i : -1).filter(i => i > 0),
    emptyX: [...Array(map[0].length).keys()].map(x  => [...Array(map.length).keys()].every(y => map[y][x] == '.') ? x : -1).filter(i => i > 0)
  }
}

const pairGalaxies = (galaxyPositions) => {
  const pairs = [];
  for(let i = 0; i < galaxyPositions.length - 1; i++) {
    for(let j = i + 1; j < galaxyPositions.length; j++) {
      pairs.push([galaxyPositions[i], galaxyPositions[j]]);
    }
  }
  return pairs;
}

const calculateDistances = (galaxyPairs, expansionRatio, navChart) => {
  return galaxyPairs.map(pair => {
    const a = pair[0];
    const b = pair[1];
    const primaryDistance = Math.abs(a.x - b.x) + Math.abs(a.y - b.y)
    const crossXCount = navChart.emptyX.filter(x => x < Math.max(a.x, b.x) && x > Math.min(a.x, b.x)).length;
    const crossYCount = navChart.emptyY.filter(y => y < Math.max(a.y, b.y) && y > Math.min(a.y, b.y)).length;
    return primaryDistance - crossXCount - crossYCount + (crossXCount * expansionRatio) + (crossYCount * expansionRatio);
  })
}

const input = tools.getInput2DArray(1);
console.log("==== Answers ====");
solve(input);
