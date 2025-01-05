import math
puzzleInput = """.....................5...............P............
.............w.....T.........Xh.....5............u
...................kX.......T.......H.P...........
......u.....k...E..............................P..
.....................F.........................o..
...............k........F...................o.....
...............E........x...k..w......S..........a
...................E.......9..x.....P.............
...............................X..................
..............................................X.a.
............A.............w........e...u..........
..T...................9........x....B..........H..
..........Z.....................u.5...........3...
....................d..F.....5...zC..B...S........
...............TfZ..........F.........7S..e.h...o.
....................................3e.........h..
.....A...............f.........Hb....3O...........
..............f..d...............................o
......................................4...........
......g...................H..Z.........C.3.4..e...
............p.....d......................x...h....
...............f.p.....................l.......M..
..................................a............l..
........A.............j..........G................
...N...............9.......r..B.z.....C...........
............................lg......4..........7S.
................K.......Ey.......4.g...........V.7
........N......Av...............................G.
.............b...K...B...................C......V.
...........K...................r.....a............
.................................v...Mg...........
......p.....Z..........jr.....Y........J.....O..7.
.....p....N.....t..........j...O............l.....
.....................L...Ut.....O..v.....V........
.d......D...W......n....j0..................s..G..
.....y........L.........s...0nV.c.M...8...........
...........L.............................J..G.....
...D.................2............J..R............
.......m................L.2.....vU8Rc.............
....................................n..cz..s......
..y....................2.......c..................
............w....0....2....8....1.R.6.............
.............................86...r...........Y...
KN..............m.................U...............
.................t....n.0........1..J..z..........
......D........................1..................
m..................W......R......61...M..........Y
y....................W.b...m...................Y..
.....D....................U............s..........
..............W..6...........tb..................."""

test = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

def mapParse(input):
    output = []
    for lines in input.split('\n'):
        inner = []
        for element in lines:
            inner.append(element)
        output.append(inner)
    return output

def displayMap(input):
    for lines in input:
        strLines = ""
        for element in lines:
            strLines += element
        print(strLines)

def uniqueSignal(map):
    signal = set()
    for lines in map:
        for item in lines:
            if item != '.':
                signal.add(item)
    return signal

def markNode(map, signal):
    print(signal)
    pos = {}
    antinodes = set()
    for element in signal:
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == element:
                    pos.setdefault(element, []).append((i, j))
    
    def triangulate(pos1, pos2):
        antinodes = []
        diffRow = abs(pos1[0] - pos2[0])
        diffCol = abs(pos1[1] - pos2[1])
        # downslope
        if (pos1[0] <= pos2[0] and pos1[1] < pos2[1]) or (pos1[0] >= pos2[0] and pos1[1] > pos2[1]):
            newPos1 = (min(pos1[0], pos2[0]) - diffRow, min(pos1[1], pos2[1]) - diffCol)
            newPos2 = (max(pos1[0], pos2[0]) + diffRow, max(pos1[1], pos2[1]) + diffCol)
        # upslope
        elif (pos1[0] < pos2[0] and pos1[1] > pos2[1]) or (pos1[0] > pos2[0] and pos1[1] < pos2[1]):
            newPos1 = (min(pos1[0], pos2[0]) - diffRow, max(pos1[1], pos2[1]) + diffCol)
            newPos2 = (max(pos1[0], pos2[0]) + diffRow, min(pos1[1], pos2[1]) - diffCol)
        # vert
        elif (pos1[1] == pos2[1]):
            newPos1 = (min(pos1[0], pos2[0]), pos1[1])
            newPos2 = (max(pos1[0], pos2[0]), pos1[1])
        # horizontal
        elif (pos1[0] == pos2[0]):
            newPos1 = (pos1[0], min(pos1[1], pos2[1]))
            newPos2 = (pos1[0], max(pos1[1], pos2[1]))
        # check valid positions
        if newPos1[0] >= 0 and newPos1[0] < len(map) and newPos1[1] >= 0 and newPos1[1] < len(map[0]):
            antinodes.append(newPos1)

        if newPos2[0] >= 0 and newPos2[0] < len(map) and newPos2[1] >= 0 and newPos2[1] < len(map[0]):
            antinodes.append(newPos2)
        return antinodes
    # pos now has a list of position
    def generatePairs(input):
        pairs = []
        for i in range(len(input)):
            for j in range(i + 1, len(input)):
                pairs.append((input[i], input[j]))
        return pairs

    for element in signal:
        towers = pos.get(element)
        if len(towers) == 1:
            continue
        allPairs = generatePairs(towers)
        for pair in allPairs:
            for i in (triangulate(pair[0], pair[1])):
                antinodes.add(i)
    
    for element in antinodes:
        if map[element[0]][element[1]] == '.' or map[element[0]][element[1]] == '#':
            map[element[0]][element[1]] = '#'

    print(displayMap(map))
    print(len(antinodes))

# displayMap(mapParse(test))
# uniqueSignal(mapParse(test))
input = puzzleInput
markNode(mapParse(input), uniqueSignal(mapParse(input)))
