import time
def parseInput(input):
    output = []
    for row in input.strip().split('\n'):
        innerArray = []
        for element in row:
            innerArray.append(element)
        output.append(innerArray)
    return output

def findGuard(arr):
    guardPos = (None, None)
    row = 0
    for y in arr:
        col = 0
        for x in y:
            if x == '^':
                guardPos = (col, row)
            col += 1
        row += 1
    return guardPos


def guardMove(guardPos, arr, direction, barrier):
    newObstacleCount = 0
    loopCheck = 0
    if loopCheck > 10:
        return 1
    # while guard is within map, guard is valid to move
    while (guardPos[0] < len(arr[0]) and guardPos[0] >= 0) and (guardPos[1] < len(arr) and guardPos[1] >= 0):
        currentPos = guardPos
        # mark current position
        currentX = currentPos[0] 
        currentY = currentPos[1]
        if arr[currentY][currentX] == '.':
            new = True
        else:
            new = False
            loopCheck += 1

        # next position
        nextx = guardPos[0]
        nexty = guardPos[1]
        nextPos = guardPos
        # move up
        if direction == 0:
            arr[currentY][currentX] = '|'
            nextPos = (nextx, nexty - 1) 
        # move down
        elif direction == 2:
            arr[currentY][currentX] = '|'
            nextPos = (nextx, nexty + 1)
        # move left
        elif direction == 3:
            arr[currentY][currentX] = '-'
            nextPos = (nextx - 1, nexty)
        # move right
        elif direction == 1:
            arr[currentY][currentX] = '-'
            nextPos = (nextx + 1, nexty)

        invalidRoute = 0
        if barrier == 1:
            tempNext = arr[nexty][nextx]
            arr[nexty][nextx] = 'O'
            # alternate position
            altx = guardPos[0]
            alty = guardPos[1]
            altPos = guardPos
            if direction == 0:
                altPos = (altx + 1, alty)
                altdirection = 1
            elif direction == 1:
                altPos = (altx, alty + 1)
                altdirection = 2
            elif direction == 2:
                altPos = (altx - 1, alty)   
                altdirection = 3
            elif direction == 3:
                altPos = (altx, alty - 1)
                altdirection = 0
            arr[guardPos[1]][guardPos[0]] = '+'
            invalidRoute = guardMove(altPos, arr, altdirection, barrier - 1)


        if new == False:
            arr[currentY][currentX] = '+'

        if not((nextPos[0] < len(arr[0]) and nextPos[0] >= 0) and (nextPos[1] < len(arr) and nextPos[1] >= 0)):
            break  

        if arr[nextPos[1]][nextPos[0]] == '#' or arr[nextPos[1]][nextPos[0]] == 'O':
            arr[currentY][currentX] = '+'
            if direction == 0:
                nextPos = (nextx + 1, nexty)
                direction = 1
            elif direction == 1:
                nextPos = (nextx, nexty + 1)
                direction = 2
            elif direction == 2:
                nextPos = (nextx - 1, nexty)
                direction = 3
            elif direction == 3:
                nextPos = (nextx, nexty - 1)
                direction = 0
        guardPos = nextPos                                                   
    return newObstacleCount + invalidRoute

def countPath(arr):
    count = 0
    for row in arr:
        count +=  row.count('X')
    return count

def print2d(arr):
    str = ""
    for row in arr:
        curr = ""
        for element in row:
            curr += element
        str += curr + "\n"
    print(str)
    return

test = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''

puzzleInput = '''...#....#................................#..........................#..........#.............#..#.................................
.......#........................#.......#......................#............#.....................................................
..#......#....................................................................................#.......#................#..........
..................#...........#...#..#............................#.........#...................#...............................#.
..#...................................................................................................................#....#......
............#.............................#......................#.......#...........#..................##..............#.........
..............................#................................................#.............................................#....
....................#.#...........#...#....#..............#.........#.........#..................#...........#.................#..
.#........................................................................#.....#.......##.....................#..................
.#........................#..................................#............................#...#..........#.......#.............#..
................................#......#...............#...........................#.............................#..#.#...#....#..
..........................................................#..........#..#.......#........#............#.................#.........
......#.......#......................................................................................#................#...........
##......#...................................................#................#............................#.......................
.....#.................................................................#.....................#...............................#...#
...........................................................................................................#......................
........#......................#..........#..#....#....................#..##...........#..#.............................#.#......#
#...#..................#.....................#...#...#.......................................................#.....#..............
#...#..................#.#....#...............#...........#...................#.....##......................................#.....
......#............................................................................................#...#.#........................
......................................................#..............#.....#.....#..#...........#..............................#..
.........................##.#..............#............#....................................................................##...
..#....................#...........................................................................................#......#.##....
..............#........#..#.......#................#.....#.......................................................................#
.........#..........................#........#..........#...............#...................................#.............#.......
...........#.....................#.....#..............#......#.........................................#..........................
.......##.............................#.........#...............#...............#..............................................#..
.......#.....#.....#...........#............................................................................#..............#.....#
....#.............................................#....#....#....#...........................................##..............##...
.#.............#.......#.....#.........#....#......#.............#............#......#............#......................#........
..................................................................................................#....#..........................
.............................................#....................#...............................#.............#.................
.........#...............#.....................#...............#......#.................................................#.........
..........#.................................................................................#..............#..............#.....#.
.........................#........#.....#............#.....................#.......................................#..............
.....................#.....................#..............................#..................................#..........#.........
........................#.....................#..............................#.#................#.................................
.....................................................#...............#.......................................................#....
.................#.......#......##..............................##.................#..........................#....#....#........#
.............................#................................#..#...........#..........#.........................................
.#...........................#........#.#...#...#....#......#......#...........#..................##.........................#....
.......................................#......................................#................................................#..
..........##......#..............................................................#.......#....................#..#......#.........
.#...............#............#....#....................................^......#.........................................#.#......
.................#....................#..#....#.......................#.............................#.....#.....#............#....
...............................................................#...............##.................#........#.#....................
...................................#..#.........#.........#...............#.........#.......................................#.....
.........................#......................................................................................#............#....
.................................#............#............#.............................#........................................
..........#.........#...........................................#..#...#..#.......................................................
.#....#....#..........................................#.....#..........................................................#..........
...#...............#......................................................................#.............................#.........
....#......................#...........#......................................#..............#...........................#........
.......................................................#...........#.......#..............................#.......................
......#............#.#...........#............#...................#..................#................................##..........
.......#..........................................................................................#.....................##........
....................................#.........#..................##....................#.#...........#......................#.....
.........................#...............................................................#....................#...................
...............................#........................................................................#....................#....
..#.#.......................................................................#..........#.........#........#.......................
....#....#.....................#.............#..#........................#.............#.....#....................................
..#............................................................................#....................#.................#.....#.#...
..............................................#........#............##.#..............#...#...................#...................
.............................#..................#..................#.................................#............................
......#................................#....#..................................#............#.....................................
#..........#...#..................#...............................................................................................
......................................#......................................#.......#....#.......................................
......................................................................#......................................#...........##.....#.
.......#.............#................................................#.....#..#......#......................................#....
..........................................#...............#...#........#..........................................................
#..#......#..........#....#.......................................................................................................
.......#..#............................................................#........#...#.#...........................................
.#....#...#..#................................................#......................#............................................
.........................#...........#..........#............#...............................#...#...#..................#.........
....#......................#......#.......#....................#..........................#...............................#.......
.........................#...............#.........................#.........#..................................#.................
...............................#......................................................#...........................................
..................................................#.........................#...................#......#..........................
...................#.##..............................#................#........#..............................#...................
.#.................#..............................#................#............................#............#................#...
............#..............#....................................#.....#.....#..........#................#.........................
...................#.............................#...........##...........................................#.......................
.#.............##...........#............##...#.........................................................................#.......#.
........#................#....................#..........#....#.......#.#..............#..............#.................#.........
............................#..#...#..........................................................#......#............................
.........#.................#......#.............................................#...##.....#.................................##...
............#..........................................................................#..........#...................#...........
....................................#.............#............#..................#....#.#.......................#...#............
......#...................................................##....................................................................#.
...............................#.............#.#...............#.......................................#.#.......................#
..........#............................#....#.#.#.#..............................................................#................
....#...#............#.#.................................................#.....................................#.#................
...........#...............................##.........#............#.....................#........................................
...................#.............................#.........#..............................................#.....#.................
.........#................#.........#.............#.............#...#...........................................................#.
.....#...........................#............##............#................#...............................#.............#..#...
................#.#.......#.................#...................................................#.........#..........##.#.........
.........................#.................#...............#...........................#............#.............#..............#
...................#......#...........................#.....#.....................................................#...............
......#...........##......#..................#......#............##................................#..............................
....................#.........#...........................................................................................#....#..
................................................#....#.....#..#........................#....................##....................
........#...........#....#.......#..........##............................................#.......#.........#...#...............#.
#.#.....#.#..............................................#...#...............#..........#................##.........#..........#.#
#........................#...#.........#........#..............................................................#..................
..................................................................................................................................
...........................................#..#..........................................#...................#....................
...................#.............#.....#..................................................#...................................#...
................#...........................................................................#.#...#...............................
........#.......#......#...........................................#....................................#......#............#.....
...............#.......#....................#.....................................................................#...............
..............##....#.............................#......................#.....#......#........................................#..
............................#.........#.....................#.....................................................................
#....................#...................##........#...#........#......#....#..........................................#.#.......#
..#............#...#...............................#.#....................#....................................#..............#...
..................#..#.......#......#.....#.......#.................#.....#...................................#.............#.....
.......................#..............#.........#............#.......#.................................................#.....#....
................#.....................................................#.#.............................#.........#...........#.....
......................#.................................##..................................#.................................#...
.......................................#........................................................................#.................
.........#...........#..............#......................#................................#..#.......................#..........
...................#..................#...#....#......................................................#...........................
..............................#.........#................................#............................#...........................
........#....#...................................................................##........#......................................
..................................#...................#...................#.#.......#.............#..............................#
.....................................#...##...............................................................................#.......
......................#.......#.............#.......................#..#.....#......................#.................#...........
.....##...........#.......#................#.................................#...##......#......#...............#.......#.#.......
.....#...#...............#......................#........#..........#..##...#...#........#..........#.............................
#...........#.............#...............................#..............................#...#.#........#.........................'''

currentInput = test
print(guardMove(findGuard(parseInput(currentInput)), parseInput(currentInput), 0, 1))
