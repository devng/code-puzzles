// http://beachhackathon.com/resources/icancode/epam-landing.html#play
// http://beachhackathon.com/codenjoy-contest/resources/icancode/landing-icancode-training.html
// https://github.com/codenjoyme/codenjoy/tree/master/CodingDojo/games

const OBSTACLES = ["HOLE", "BOX", "WALL", "LASER_MACHINE", "LASER_MACHINE_READY", "LASER_LEFT", "LASER_RIGHT", "LASER_UP", "LASER_DOWN"];

const LASERS = ["LASER_MACHINE_READY", "LASER_LEFT", "LASER_RIGHT", "LASER_UP", "LASER_DOWN"]

const JUMP_OVER = ["HOLE", "BOX"];

var visitedPoints = [];

function program(robot) {
    var scanner = robot.getScanner();
    visitedPoints.push(scanner.getMe());
    
    var possibleMoves = getPossibleMoves(robot);
    var possibleJumps = getPossibleJumps(robot);
    var allActions = possibleJumps.concat(possibleMoves);
    scoreMoves(robot, allActions);
    var a = allActions[0];
    if (a.type == "JUMP") {
        robot.jump(a.d);
    } else {
        robot.go(a.d);
    }
}

function isPointVisited(x, y) {
    return isPointInArray(x, y, visitedPoints);
}

function isPointInArray(x, y, arr) {
    for (var i = 0; i < arr.length; i++) {
        if (x == arr[i].x && y == arr[i].y) {
            return true;
        }
    }
    return false;
}

function isObstacle(s) {
    return isAnyOf(s, OBSTACLES);
}

function canJumpOver(s) {
    return isAnyOf(s, JUMP_OVER);
}

function isAnyOf(s, arr) {
    if (Array.isArray(s)) {
        for (var i = 0; i < s.length; i++) {
            if (arr.includes(s[i])) {
                return true;
            }
        }   
    } else {
        return arr.includes(s);
    }
    return false;
}

function scoreMoves(robot, actions) {
    var scanner = robot.getScanner();
    var goldPoints = scanner.getGold();
    var destinationPoints = goldPoints.concat(scanner.getExit());
    var path = scanner.getShortestWay(destinationPoints[0]);

    for (var i = 0; i < actions.length; i++) {
        var a = actions[i];
        if (isPointInArray(a.x, a.y, path)) {
            a.s += 10;
        }
        if (isPointInArray(a.x, a.y, goldPoints)) {
            a.s += 20;
        }
        if (isPointVisited(a.x, a.y)) {
            a.s -= 15;
        }
        if (scanner.getAt(a.x, a.y) == "EXIT" && goldPoints.length > 0) {
            a.s -= 100;
            visitedPoints = [scanner.getMe()];
        }
        if (scanner.isNear(a.x, a.y, LASERS)) {
            a.s -= 20; 
        }
        if (a.type == "JUMP") {
            a.s = a.s + 5;
        }
    }
    // robot.log("possible actions: " + actions);
    actions.sort(function (a, b) {
        return b.s - a.s;
    });
}

function getPossibleJumps(robot) {
    var scanner = robot.getScanner();
    var possibleJumps = [];
    var cp = scanner.getMe();
    if (canJumpOver(scanner.atNearRobot(0, +1)) && !isObstacle(scanner.atNearRobot(0, +2))) {
        possibleJumps.push({d: "DOWN", x: cp.x, y: cp.y + 2, s: 0, type: "JUMP"});
    }
    if (canJumpOver(scanner.atNearRobot(0, -1)) && !isObstacle(scanner.atNearRobot(0, -2))) {
        possibleJumps.push({d: "UP", x: cp.x, y: cp.y - 2, s: 0, type: "JUMP"});
    }
    if (canJumpOver(scanner.atNearRobot(+1, 0)) && !isObstacle(scanner.atNearRobot(+2, 0))) {
        possibleJumps.push({d: "RIGHT", x: cp.x + 2, y: cp.y, s: 0, type: "JUMP"});
    }
    if (canJumpOver(scanner.atNearRobot(-1, 0)) && !isObstacle(scanner.atNearRobot(-2, 0))) {
        possibleJumps.push({d: "LEFT", x: cp.x - 2, y: cp.y, s: 0, type: "JUMP"});
    }
    // robot.log("possible jump: " + possibleJumps);
    return possibleJumps;
}


function getPossibleMoves(robot) {
    var scanner = robot.getScanner();
    var cp = scanner.getMe();
    var possibleMoves = [];
    if (!isObstacle(scanner.atDown())) {
        possibleMoves.push({d: "DOWN", x: cp.x, y: cp.y + 1, s: 0, type: "MOVE"});
    }
    if (!isObstacle(scanner.atUp())) {
        possibleMoves.push({d: "UP", x: cp.x, y: cp.y - 1, s: 0, type: "MOVE"});
    }
    if (!isObstacle(scanner.atLeft())) {
        possibleMoves.push({d: "LEFT", x: cp.x - 1, y: cp.y, s: 0, type: "MOVE"});
    }
    if (!isObstacle(scanner.atRight())) {
        possibleMoves.push({d: "RIGHT", x: cp.x + 1, y: cp.y, s: 0, type: "MOVE"});
    }
    // robot.log("possible moves: " + possibleMoves);
    return possibleMoves;
}
