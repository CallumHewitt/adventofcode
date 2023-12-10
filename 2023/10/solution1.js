const tools = require("./tools");

const solve = (map) => {
  const start = findStart(map);
  const route = trackRoute(map, start);
  console.log("Q1:", Math.ceil(route.length / 2) - 1);
  const indexedRoute = indexRoute(route);
  const enclosedGroundCount = countEnclosedGround(map, indexedRoute);
  console.log("Q2:", enclosedGroundCount);
};

const findStart = (map) => {
  const locations = tools.findLocationsOfValue(map, "S");
  if (locations.length != 1) {
    throw new Error(`Found ${locations.length} starting positions. ${JSON.stringify(locations)}`);
  }
  return locations[0];
};

const trackRoute = (map, start) => {
  const startDetails = findStartDetails(map, start)
  const newStart = {
    x: start.x, y: start.y, value: startDetails.replacement
  }
  const route = [newStart, startDetails.next];
  while (!(route.at(-1).x == start.x && route.at(-1).y == start.y)) {
    const nextPosition = findNextPosition(map, route.at(-1), route.at(-2));
    route.push(nextPosition);
  }
  return route.slice(0, -1);
};

const findStartDetails = (map, start) => {
  let potentialReplacements = ['|', '-', 'F', '7', 'J', 'L'];
  let adjacentPoints = [];
  const north = tools.findNorth(map, start.x, start.y);
  if (["F", "|", "7"].includes(north.value)) {
    potentialReplacements = potentialReplacements.filter(i => !['-', '7', 'F'].includes(i));
    adjacentPoints.push(north);
  }
  const east = tools.findEast(map, start.x, start.y);
  if (["7", "-", "J"].includes(east.value)) {
    potentialReplacements = potentialReplacements.filter(i => !['|', 'J', '7'].includes(i));
    adjacentPoints.push(east);
  }
  const south = tools.findSouth(map, start.x, start.y);
  if (["L", "J", "|"].includes(south.value)) {
    potentialReplacements = potentialReplacements.filter(i => !['-', 'L', 'J'].includes(i));
    adjacentPoints.push(south);
  }
  const west = tools.findWest(map, start.x, start.y);
  if (["F", "-", "L"].includes(west.value)) {
    potentialReplacements = potentialReplacements.filter(i => !['|', 'F', 'L'].includes(i));
    adjacentPoints.push(south);
  }
  if (adjacentPoints.length != 2 || potentialReplacements.length != 1) {
    throw new Error(`Issue with replacing the start point: ${JSON.stringify(adjacentPoints)}, ${JSON.stringify(potentialReplacements)}`);
  }
  return {
    next: adjacentPoints[0],
    replacement: potentialReplacements[0]
  }
}

const findNextPosition = (map, point, previousPoint) => {
  switch (point.value) {
    case "|": {
      if (previousPoint.y < point.y) {
        return tools.findSouth(map, point.x, point.y);
      } else {
        return tools.findNorth(map, point.x, point.y);
      }
    }
    case "-": {
      if (previousPoint.x > point.x) {
        return tools.findWest(map, point.x, point.y);
      } else {
        return tools.findEast(map, point.x, point.y);
      }
    }
    case "L": {
      if (previousPoint.y < point.y) {
        return tools.findEast(map, point.x, point.y);
      } else {
        return tools.findNorth(map, point.x, point.y);
      }
    }
    case "J": {
      if (previousPoint.y < point.y) {
        return tools.findWest(map, point.x, point.y);
      } else {
        return tools.findNorth(map, point.x, point.y);
      }
    }
    case "7": {
      if (previousPoint.x < point.x) {
        return tools.findSouth(map, point.x, point.y);
      } else {
        return tools.findWest(map, point.x, point.y);
      }
    }
    case "F": {
      if (previousPoint.x > point.x) {
        return tools.findSouth(map, point.x, point.y);
      } else {
        return tools.findEast(map, point.x, point.y);
      }
    }
    case ".": {
      throw new Error(`Off the pipe at ${point} having come from ${previousPoint}`);
    }
    case "S": {
      throw new Error(`Failed to break after reaching the start again.`);
    }
  }
};

const indexRoute = (route) => {
  return route.map((p, i) => ({
    x: p.x,
    y: p.y,
    value: p.value,
    index: i,
  }));
};

const countEnclosedGround = (map, route) => {
  const maxX = Math.max.apply(
    Math,
    route.map((p) => p.x)
  );
  const maxY = Math.max.apply(
    Math,
    route.map((p) => p.y)
  );
  const minX = Math.min.apply(
    Math,
    route.map((p) => p.x)
  );
  const minY = Math.min.apply(
    Math,
    route.map((p) => p.y)
  );
  let enclosedCount = 0;
  console.log(route);
  for (let y = minY; y <= maxY; y++) {
    let rayCastCount = 0;
    for (let x = minX; x <= maxX; x++) {
      const routePiece = route.find((p) => p.x == x && p.y == y);

      if (!routePiece) {
        console.log(`Did not find route piece at ${x}, ${y}`);
        if (rayCastCount % 2 == 1) {
          console.log(x, y, "is enclosed.");
          enclosedCount++;
        } else {
          console.log(x, y, "is not enclosed.");
        }
      } else {
        console.log(`Found route piece at ${x}, ${y}`);
        if (routePiece.value == '-' || routePiece.value == '7' || routePiece.value == 'J') {
          // Ignore, you already hit the corner earlier.
        } else if (routePiece.value == '|' || routePiece.value == 'L' || routePiece.value == 'F') {
          console.log("Incrementing ray cast count.");
          rayCastCount++;
        }
      }
    }
  }
  return enclosedCount;
};

const input = tools.getInput2DArray(0);
solve(input);