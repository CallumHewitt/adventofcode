const tools = require("./tools");

const solve1 = (input) => {
  const map = parseMap(input);
  return navigateMap(map, 'AAA', 'ZZZ')
};

const parseMap = (input) => {
  const directions = input[0].split('');
  const nodes = input.slice(2)
    .map(line => {
      const match = line.match(/([A-Z]{3}) =.*([A-Z]{3}).*([A-Z]{3})/)
      return [match[1], match[2], match[3]]
    })  
    .reduce((acc, c) => ({...acc, [c[0]]: [c[1], c[2]]}), {})
  return {
    directions, nodes
  }
}

const navigateMap = (map, start, goal) => {
  let count = 0
  let current = start;
  while(current != goal) {
    const direction = map.directions[count % map.directions.length]
    if (direction == 'L') {
      current = map.nodes[current][0];
    } else {
      current = map.nodes[current][1];
    }
    count++;
  }
  return count;
}

const solve2 = (input) => {
  const map = parseMap(input);
  return navigateGhostMap(map, 'A', 'Z')
};

const navigateGhostMap = (map, startKey, goalKey) => {
  const currents = Object.keys(map.nodes).filter(node => node.endsWith(startKey));
  const distances = currents.map(current => {
    let count = 0;
    while(!current.endsWith(goalKey)) {
      const direction = map.directions[count % map.directions.length]
      if (direction == 'L') {
        current = map.nodes[current][0];
      } else {
        current = map.nodes[current][1];
      }
      count++;
    }
    return count;
  });
  // Nothing in the problem statement guarantees this works. It just does.
  return tools.lowestCommonMultipleRange(distances);
}

const input = tools.getInputList(1);
console.log("==== Answers ====");
console.log("Q1:", solve1(input));
console.log("Q2:", solve2(input));