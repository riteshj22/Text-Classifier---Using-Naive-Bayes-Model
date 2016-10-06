import sys
import string
import copy

globalcounter = 0


# mapping numbers to alphabets
mapping_list = string.ascii_uppercase

# ################ filename as command line arguments#############
filename = sys.argv[-1]

# Reading the input file
inputFile = open(filename, "r")

list1 = []
temp_list = []

# f1 = open("traverse_log.txt", "w")


# line by line reading without newline character
content = inputFile.read().splitlines()
inputFile.close()
# print content
# row index for 2d list

r = 0


# Display

def display(data_list):
    if data_list:
        for a in range(0, board_size, 1):
            for b in range(0, board_size, 1):
                print data_list[a][b],
            print "\n"
    else:
        print "No data to display"


def find_neighbours(arr):
    p = []
    l1 = []
    mov = []
    flag = 0
    temp_x = 0
    temp_y = 0

    for i in range(0, board_size, 1):

        for j in range(0, board_size, 1):
            flag = 0
            if arr[i][j] != ".":
                temp_x = i
                temp_y = j
                # l1 = adjacent_elements(i, j)
                for neighbour_x, neighbour_y in [(i + m, j + n) for m in (-1, 0, 1) for n in (-1, 0, 1)]:
                    if temp_x == neighbour_x and temp_y == neighbour_y:
                        continue
                    else:
                        if neighbour_y <= board_size - 1 and neighbour_x <= board_size - 1:
                            if arr[neighbour_x][neighbour_y] == ".":

                                m = [neighbour_x, neighbour_y]
                                flag = 0
                                # for move in mov:
                                #     if move == m:
                                #         flag = 1
                                if m not in mov:
                                    flag = 1

                                if flag == 1:
                                    if 0 <= neighbour_x <= board_size - 1 and 0 <= neighbour_y <= board_size - 1:
                                        mov.append(m)
    return mov


def e(c_me, c_opp, openn, closed):
    if c_me == 2:

        if openn == 1:
            return 5
        elif closed == 1:
            return 0
        elif not openn and not closed:
            return 1
        else:
            return 0

    if c_me == 3:

        if openn == 1:
            return 50
        elif not openn and not closed:
            return 10
        else:
            return 0
    if c_opp == 3:
        if closed == 1:
            return 100

        elif not openn and not closed:
            return 500
        else:
            return 0
    if c_me == 4:
        if openn == 1:
            return 5000

        elif not openn and not closed:
            return 1000
        else:
            return 0
    if c_opp == 4:
        if closed == 1:
            return 10000
        else:
            return 0

    if c_me == 5 or c_opp == 5:
        return 50000
    else:
        return 0


def lp(temp_list2, x, y, p1, p2):
    mer = 0
    me = 0
    mel = 0
    u = x
    v = y
    opp = 0
    openn = 0
    closed = 0
    block_right = 0
    block_left = 0
    left = 0
    right = 0
    size = len(temp_list2)

    # right
    while y + 1 <= size - 1:

        if temp_list2[x][y + 1] == ".":
            break
        while temp_list2[x][y + 1] == p1:
            mer += 1
            y += 1
            if y + 1 == board_size:
                block_right = 1
                break

            if temp_list2[x][y + 1] == p2:
                block_right = 1
                break

        if block_right == 1 and mer != 0:
            break

        if mer == 0:
            while temp_list2[x][y + 1] == p2:
                opp += 1
                y += 1

                if y + 1 == board_size:
                    block_right = 1
                    break

                if temp_list2[x][y + 1] == p1:
                    block_right = 1
                    break

            block_left = 1
            break

    if block_left and block_right:
        closed = 1

    if not block_right and not block_left:
        openn = 1
    # print mer, opp

    if opp > 1:
        right = e(mer, opp, openn, closed)
        # print "right", right

    # left
    x = u
    y = v
    opp = 0
    block_right = 0
    block_left = 0
    openn = 0
    closed = 0
    while y - 1 >= 0:

        if temp_list2[x][y - 1] == ".":
            break
        while temp_list2[x][y - 1] == p1:
            mel += 1
            y -= 1

            if y - 1 < 0:
                block_right = 1
                break

            if temp_list2[x][y - 1] == p2:
                block_right = 1
                break
        if block_right == 1 and mel != 0:
            break

        if mel == 0:
            while temp_list2[x][y - 1] == p2:
                opp += 1
                y -= 1

                if y - 1 < 0:
                    block_left = 1
                    break

                if temp_list2[x][y - 1] == p1:
                    block_left = 1

            block_right = 1
            break

    if block_left and block_right:
        closed = 1

    if not block_right and not block_left:
        openn = 1
    # print mel, opp

    if opp > 1:
        left = e(mel, opp, openn, closed)
        # print "left", left

    # horizontal
    block_left = 0
    block_right = 0
    openn = 0
    closed = 0
    opp > 0
    x = u
    y = v
    me = mel + mer + 1
    horiz = 0
    if y + 1 == board_size:
        block_right = 1
    else:
        if temp_list2[x][y + 1] == p2:
            block_right = 1

        else:
            while temp_list2[x][y + 1] == p1:
                y += 1
                if y + 1 == board_size:
                    block_right = 1
                    break
                if temp_list2[x][y + 1] == p2:
                    block_right = 1
    y = v

    if y - 1 < 0:
        block_left = 1
    else:
        if temp_list2[x][y - 1] == p2:
            block_left = 1
            while  temp_list2[x][y-1] == p2:
                y -= 1
        else:
            while temp_list2[x][y - 1] == p1:
                y -= 1
                if y - 1 < 0:
                    block_left = 1
                    break
                if temp_list2[x][y - 1] == p2:
                    block_left = 1

    if temp_list2[x][y-1] == p1 and block_left == 1 and me == 1:
        block_right = 1
    if block_left and block_right:
        closed = 1


    if not block_right and not block_left:
        openn = 1

    h = e(me, opp, openn, closed)
    # print "hori", h

    if h == left and opp > 1:
        left = 0

    horiz = h + left + right
    # print horiz

    # up

    x = u
    y = v
    openn = 0
    closed = 0
    meu = 0
    med = 0
    opp = 0
    up = 0
    down = 0
    block_up = 0
    block_down = 0
    while x - 1 >= 0:
        if temp_list2[x - 1][y] == ".":
            break
        while temp_list2[x - 1][y] == p1:
            meu += 1
            x -= 1

            if x - 1 < 0:
                block_up = 1
                break

            if temp_list2[x - 1][y] == p2:
                block_up = 1
                break
        if block_up == 1 and meu != 0:
            break

        if meu == 0:
            while temp_list2[x - 1][y] == p2:
                opp += 1
                x -= 1

                if x - 1 < 0:
                    block_up = 1
                    break

                if temp_list2[x - 1][y] == p1:
                    block_up = 1

            block_down = 1
            break

    if block_up and block_down:
        closed = 1

    if not block_up and not block_down:
        openn = 1
    # print meu, opp

    if opp > 1:
        up = e(meu, opp, openn, closed)
        # print "up", up

    # down

    x = u
    y = v
    openn = 0
    closed = 0
    opp = 0
    block_up = 0
    block_down = 0

    while x + 1 <= size - 1:

        if temp_list2[x + 1][y] == ".":
            break
        while temp_list2[x + 1][y] == p1:
            med += 1
            x += 1

            if x + 1 == board_size:
                block_down = 1
                break

            if temp_list2[x + 1][y] == p2:
                block_down = 1
                break

        if block_down == 1 and med != 0:
            break

        if med == 0:
            while temp_list2[x + 1][y] == p2:
                opp += 1
                x += 1

                if x + 1 == board_size:
                    block_down = 1
                    break

                if temp_list2[x + 1][y] == p1:
                    block_down = 1

            block_up = 1
            break

    if block_up and block_down:
        closed = 1

    if not block_up and not block_down:
        openn = 1
    # print med, opp

    if opp > 1:
        down = e(med, opp, openn, closed)
        # print "down", down

    # vertical

    block_up = 0
    block_down = 0
    me = meu + med + 1
    x = u
    y = v
    opp = 0
    openn = 0
    closed = 0

    if x - 1 < 0:
        block_up = 1
    else:
        if temp_list2[x - 1][y] == p2:
            block_up = 1
        else:
            while temp_list2[x - 1][y] == p1:
                x -= 1

                if x - 1 < 0:
                    block_up = 1
                    break

                if temp_list2[x - 1][y] == p2:
                    block_up = 1

    x = u
    y = v

    if x + 1 <= size - 1:
        if temp_list2[x + 1][y] == p2:
            block_down = 1
        else:
            while temp_list2[x + 1][y] == p1:
                x += 1

                if x + 1 == board_size:
                    block_down = 1
                    break

                if temp_list2[x + 1][y] == p2:
                    block_down = 1

    if block_down and block_up:
        closed = 1

    if not block_up and not block_down:
        openn = 1

    ve = e(me, opp, openn, closed)

    # print "ver", ve

    vert = ve + up + down
    # print vert

    # diagonal forward up
    block_right = 0
    block_left = 0
    d_down = 0
    d_up = 0
    x = u
    y = v
    mer = 0
    mel = 0
    openn = 0
    closed = 0
    opp = 0
    while y + 1 <= size - 1 and x - 1 >= 0:

        if temp_list2[x - 1][y + 1] == ".":
            break
        while temp_list2[x - 1][y + 1] == p1:
            mer += 1
            y += 1
            x -= 1

            if x - 1 < 0 or y + 1 == board_size:
                block_right = 1
                break

            if temp_list2[x - 1][y + 1] == p2 and mer != 0:
                block_right = 1
                break
        if block_right == 1 and mer != 0:
            break

        if mer == 0:
            while temp_list2[x - 1][y + 1] == p2:
                opp += 1
                y += 1
                x -= 1

                if x - 1 < 0 or y + 1 == board_size:
                    block_right = 1
                    break

                if temp_list2[x - 1][y + 1] == p1:
                    block_right = 1

            block_left = 1
            break

    if block_left and block_right:
        closed = 1

    if not block_right and not block_left:
        openn = 1
    # print mer, opp

    if opp > 1:
        d_up = e(mer, opp, openn, closed)
        # print "d_up", d_up

    # diagonal forward down
    x = u
    y = v
    block_left = 0
    block_right = 0
    openn = 0
    closed = 0
    opp = 0
    while y - 1 >= 0 and x + 1 <= len(temp_list2) - 1:

        if temp_list2[x + 1][y - 1] == ".":
            break
        while temp_list2[x + 1][y - 1] == p1:
            mel += 1
            y -= 1
            x += 1

            if y - 1 < 0 or x + 1 == board_size:
                block_right = 1
                break

            if temp_list2[x + 1][y - 1] == p2 and mel != 0:
                block_right = 1
                break
        if block_right == 1 and mel != 0:
            break

        if mel == 0:
            while temp_list2[x + 1][y - 1] == p2:
                opp += 1
                y -= 1
                x += 1

                if y - 1 < 0 or x + 1 == board_size:
                    block_right = 1
                    break

                if temp_list2[x + 1][y - 1] == p1:
                    block_right = 1

            block_left = 1
            break

    if block_left and block_right:
        closed = 1

    if not block_right and not block_left:
        openn = 1
    # print mel, opp

    if opp > 1:
        d_down = e(mel, opp, openn, closed)
        # print "d_down", d_down

    # diagonal forward
    x = u
    y = v
    block_left = 0
    block_right = 0
    openn = 0
    closed = 0
    opp = 0
    me = mel + mer + 1
    if x - 1 < 0 or y + 1 == board_size:
        block_right = 1
    else:
        if temp_list2[x - 1][y + 1] == p2:
            block_right = 1
        else:
            while temp_list2[x - 1][y + 1] == p1:
                y += 1
                x -= 1

                if x - 1 < 0 or y + 1 == board_size:
                    block_right = 1
                    break

                if temp_list2[x - 1][y + 1] == p2:
                    block_right = 1

    x = u
    y = v
    if y - 1 < 0 or x + 1 == board_size:
        block_left = 1
    else:
        if temp_list2[x + 1][y - 1] == p2:
            block_left = 1
        else:
            while temp_list2[x + 1][y - 1] == p1:
                y -= 1
                x += 1

                if y - 1 < 0 or x + 1 == board_size:
                    block_left = 1
                    break

                if temp_list2[x + 1][y - 1] == p2:
                    block_left = 1
                    break

    if block_left and block_right:
        closed = 1

    if not block_right and not block_left:
        openn = 1

    d = e(me, opp, openn, closed)
    # print "diagonal forward", d

    if (d == down) and opp > 0:
        down = 0
    if (d == up) and opp > 0:
        down = 0
     # diagonal 1 value
    d1 = d + d_down + d_up

    # print d1

    # diagonal backward up
    block_right = 0
    block_left = 0
    x = u
    y = v
    mer = 0
    mel = 0
    openn = 0
    closed = 0
    db_up = 0
    db_down = 0
    opp = 0
    while x - 1 >= 0 and y - 1 >= 0:

        if temp_list2[x - 1][y - 1] == ".":
            break
        while temp_list2[x - 1][y - 1] == p1:
            mer += 1
            y -= 1
            x -= 1

            if y - 1 < 0 or x - 1 < 0:
                block_right = 1
                break

            if temp_list2[x - 1][y - 1] == p2 and mer != 0:
                block_right = 1
                break
        if block_right == 1 and mer != 0:
            break

        if mer == 0:
            while temp_list2[x - 1][y - 1] == p2:
                opp += 1
                y -= 1
                x -= 1

                if y - 1 < 0 or x - 1 < 0:
                    block_right = 1
                    break

                if temp_list2[x - 1][y - 1] == p1:
                    block_right = 1

            block_left = 1
            break

    if block_left and block_right:
        closed = 1

    if not block_right and not block_left and mer != 0:
        openn = 1
    # print mer, opp

    if opp > 1:
        db_up = e(mer, opp, openn, closed)
        # print "db_up", db_up

    # diagonal backward down
    x = u
    y = v
    block_left = 0
    block_right = 0
    openn = 0
    closed = 0
    opp = 0

    while y + 1 <= size - 1 and x + 1 <= size - 1:

        if temp_list2[x + 1][y + 1] == ".":
            break
        while temp_list2[x + 1][y + 1] == p1:
            mel += 1
            y += 1
            x += 1

            if y + 1 == board_size or x + 1 == board_size:
                block_right = 1
                break
            if temp_list2[x + 1][y + 1] == p2 and mel != 0:
                block_right = 1
                break

        if block_right == 1 and mel != 0:
            break
        if mel == 0:
            while temp_list2[x + 1][y + 1] == p2:
                opp += 1
                y += 1
                x += 1

                if y + 1 == board_size or x + 1 == board_size:
                    block_right = 1
                    break

                if temp_list2[x + 1][y + 1] == p1:
                    block_right = 1

            block_left = 1
            break

    if block_left and block_right:
        closed = 1

    if not block_right and not block_left and mel != 0:
        openn = 1
    # print mel, opp

    if opp > 1:
        db_down = e(mel, opp, openn, closed)
        # print "db_down", db_down

    # diagonal backward
    x = u
    y = v
    block_left = 0
    block_right = 0
    openn = 0
    closed = 0
    me = mel + mer + 1
    if x - 1 < 0 or y - 1 < 0:
        block_right = 1
    else:
        if temp_list2[x - 1][y - 1] == p2:
            block_right = 1
        else:
            while temp_list2[x - 1][y - 1] == p1:
                y -= 1
                x -= 1

                if y - 1 < 0 or x - 1 < 0:
                    block_right = 1
                    break

                if temp_list2[x - 1][y - 1] == p2:
                    block_right = 1

    x = u
    y = v
    if x + 1 == board_size or y + 1 == board_size:
        block_right = 1
    else:
        if temp_list2[x + 1][y + 1] == p2:
            block_left = 1
        else:
            while temp_list2[x + 1][y + 1] == p1:
                y += 1
                x += 1

                if y + 1 == board_size or x + 1 == board_size:
                    block_left = 1
                    break

                if temp_list2[x + 1][y + 1] == p2:
                    block_left = 1

    if block_left and block_right:
        closed = 1

    if not block_right and not block_left and me != 0:
        openn = 1

    db = e(me, opp, openn, closed)
    # print "diagonal backward", db

    # diagonal 2 value
    if db_down == db and opp > 0:
        db_down = 0
    d2 = db + db_up + db_down

    value = horiz + vert + d1 + d2
    # print u, v,
    # print value
    return value


def greedy(board):
    moves = find_neighbours(board)

    for a in range(0, len(moves), 1):
        # for b in range(0, 2, 1):
            # if b == 0:
        xc = moves[a][0]
            # if b == 1:
        yc = moves[a][1]
        heuristic_value = lp(board, xc, yc, player, player2)
        # print j
        moves[a].append(heuristic_value)
    # print moves
    # print len(moves)
    x = sorted(moves, key=lambda l: (l[2], l[0], -l[1]), reverse=True)
    x_cord = x[0][0]
    y_cord = x[0][1]
    # print x
    board[x_cord][y_cord] = player
    # display(board)
    f = open("next_state.txt", "w")
    for a in range(0, int(board_size), 1):
        for b in range(0, int(board_size), 1):
            f.write(board[a][b])
        f.write("\n")
    f.close()


def rec(temp1, root1, f2, cutoff):
    # global cut_of_depth
    global depth

    d = {}
    ply1 = player
    ply2 = player2
    win = 0
    # global globalcounter
    # globalcounter += 1
    # if globalcounter == 13370:
    #     print "BREAK"
    # depth += 1
    cd = 1

    if depth > cutoff:
        return
    else:
        n = find_neighbours(temp1)
        sorted_moves = sorted(n, key=lambda l: (l[1], -l[0]))
        length = len(n)
        for a in range(0, length, 1):
            # for b in range(0, 2, 1):
            # if b == 0:
            xc = sorted_moves[a][0]
            # if b == 1:
            yc = sorted_moves[a][1]
            d = {'x': xc, 'y': yc, 'value': 0, 'children': [], 'depth': depth, 'sum': 0}
            if depth % 2 != 0:
                d['value'] = 1111111
                ply1 = player
            else:
                d['value'] = -1111111
                ply1 = player2
                ply2 = player
            temp = copy.deepcopy(temp1)
            temp[xc][yc] = ply1
            h = lp(temp, xc, yc, ply1, ply2)
            if h >= 50000:
                win = 1
                if depth % 2 != 0:
                    d['value'] = root1['sum'] + h
                else:
                    d['value'] = -h + root1['sum']

            if depth % 2 != 0:
                d['sum'] = h + root1['sum']
            else:
                d['sum'] = -h + root1['sum']
            if depth == cutoff:
                if depth % 2 != 0:
                    d['value'] = root1['sum'] + h
                else:
                    d['value'] = -h + root1['sum']

            if depth == 0:
                alphabet = "root"
            else:
                alphabet = mapping_list[yc]
            line2 = alphabet + str(15 - xc) + "," + str(d['depth']) + ","
            if d['value'] == 1111111:
                line2 += "Infinity"
            elif d['value'] == -1111111:
                line2 += "-Infinity"
            else:
                line2 += str(d['value'])
            #print line2
            f2.write(line2 + "\n")
            # f2.write("\n")
            root1['children'].append(d)
            if not win:
                rec(temp, d, f2, cutoff)
                depth -= 1

            win = 0

            if root1['depth'] % 2 != 0:
                root1['value'] = min(root1['value'], d['value'])
            else:
                root1['value'] = max(root1['value'], d['value'])

            temp[xc][yc] = "."
            if root1['x'] == 0 and root1['y'] == 0:
                line1 = "root" + "," + str(root1['depth']) + ","
            else:
                line1 = mapping_list[root1['y']] + str(15 - root1['x']) + "," + str(root1['depth']) + ","
            if d['value'] == 1111111:
                line1 += "Infinity"
            elif d['value'] == -1111111:
                line1 += "-Infinity"
            else:
                line1 += str(root1['value'])
            #print line1
            f2.write(line1 + "\n")
            # f2.write("\n")


def mini_max():
    root = {'x': 0, 'y': 0, 'value': -1111111, 'children': [], 'depth': depth, 'sum': 0}
    f1 = open("traverse_log.txt", "w")
    f1.write("Move,Depth,Value" + "\n")
    # f1.write("\n")
    root_print = "root," + "0," + "-Infinity"
    f1.write(root_print + "\n")
    # f1.write("\n")
    gameboard = copy.deepcopy(temp_list)
    rec(gameboard, root, f1, cut_of_depth)
    f1.close()
    x = sorted(root['children'], key=lambda l: (l['value'], l['x'], -l['y']), reverse=True)[0]
    x_cord = x['x']
    y_cord = x['y']
    # print x
    temp_list[x_cord][y_cord] = player
    # display(board)
    f = open("next_state.txt", "w")
    for a in range(0, int(board_size), 1):
        for b in range(0, int(board_size), 1):
            f.write(temp_list[a][b])
        f.write("\n")
    f.close()


def rec1(temp, r, f2):
    global cut_of_depth
    global depth
    # global globalcounter

    prune = 0
    d = {}
    ply1 = player
    ply2 = player2
    win = 0

    depth += 1
    cd = 1
    if depth > cut_of_depth:
        return
    else:
        n = find_neighbours(temp)
        sorted_moves = sorted(n, key=lambda l: (l[1], -l[0]))
        length = len(n)
        for a in range(0, length, 1):
            # for b in range(0, 2, 1):
            # if b == 0:
            xc = sorted_moves[a][0]
            # if b == 1:
            yc = sorted_moves[a][1]
            d = {'x': xc, 'y': yc, 'value': 0, 'children': [], 'depth': depth, 'sum': 0, 'alpha': r['alpha'],
                 'beta': r['beta']}
            if depth % 2 != 0:
                d['value'] = 1111111
                ply1 = player
            else:
                d['value'] = -1111111
                ply1 = player2
                ply2 = player
            temp[xc][yc] = ply1
            h = lp(temp, xc, yc, ply1, ply2)
            if h >= 50000:
                win = 1
                if depth % 2 != 0:
                    d['value'] = r['sum'] + h
                else:
                    d['value'] = -h + r['sum']

            if depth % 2 != 0:
                d['sum'] = h + r['sum']
            else:
                d['sum'] = -h + r['sum']
            if depth == cut_of_depth:
                if depth % 2 != 0:
                    d['value'] = r['sum'] + h
                else:
                    d['value'] = -h + r['sum']

            if depth == 0:
                alphabet = "root"
            else:
                alphabet = mapping_list[yc]
            line2 = alphabet + str(15 - xc) + "," + str(d['depth']) + ","
            if d['value'] == 1111111:
                line2 += "Infinity"
            elif d['value'] == -1111111:
                line2 += "-Infinity"
            else:
                line2 += str(d['value'])

            # ALPHA
            if d['alpha'] == 1111111:
                line2 += ",Infinity"
            elif d['alpha'] == -1111111:
                line2 += ",-Infinity"
            else:
                line2 += "," + str(d['alpha'])

            # BETA
            if d['beta'] == 1111111:
                line2 += ",Infinity"
            elif d['beta'] == -1111111:
                line2 += ",-Infinity"
            else:
                line2 += "," + str(d['beta'])

            # print line2
            f2.write(line2 + "\n")
            # f2.write("\n")
            # globalcounter += 1
            # if globalcounter == 1376:
            #     print "BREAK"
            r['children'].append(d)

            if not win:
                rec1(temp, d, f2)
                depth -= 1

            win = 0

            if depth % 2 != 0:
                if d['value'] >= r['alpha']:
                    if d['value'] >= r['beta']:
                        prune = 1
                    else:
                        r['alpha'] = d['value']
                        d['alpha'] = d['value']
            else:
                if d['value'] <= r['beta']:
                    if d['value'] <= r['alpha']:
                        prune = 1
                    else:
                        r['beta'] = d['value']
                        d['beta'] = d['value']

            if r['depth'] % 2 != 0:
                r['value'] = min(r['value'], d['value'])
                # if prune != 1:
                #     r['beta'] = min(r['beta'], d['value'])
            else:
                r['value'] = max(r['value'], d['value'])
                # r['alpha'] = max(r['alpha'], d['value'])
            # if d['alpha'] <= d['beta']:
            #         prune = 1

            temp[xc][yc] = "."
            if r['x'] == 0 and r['y'] == 0:
                line1 = "root" + "," + str(r['depth']) + ","
            else:
                line1 = mapping_list[r['y']] + str(15 - r['x']) + "," + str(r['depth']) + ","
            if r['value'] == 1111111:
                line1 += "Infinity"
            elif r['value'] == -1111111:
                line1 += "-Infinity"
            else:
                line1 += str(r['value'])

            if r['alpha'] == 1111111:
                line1 += "," + "Infinity"
            elif r['alpha'] == -1111111:
                line1 += "," + "-Infinity"
            else:
                line1 += "," + str(r['alpha'])

            if r['beta'] == 1111111:
                line1 += "," + "Infinity"
            elif r['beta'] == -1111111:
                line1 += "," + "-Infinity"
            else:
                line1 += "," + str(r['beta'])
            # print line1

            f2.write(line1 + "\n")
            # f2.write("\n")
            if prune == 1 or r['beta'] <= r['alpha']:
                break


def alpha_beta():
    root = {'x': 0, 'y': 0, 'value': -1111111, 'children': [], 'depth': depth, 'sum': 0, 'alpha': -1111111,
            'beta': 1111111}
    f1 = open("traverse_log.txt", "w")
    # print "Move,Depth,Value,Alpha,Beta"
    f1.write("Move,Depth,Value,Alpha,Beta\n")
    # f1.write("\n")
    root_print = "root," + "0," + "-Infinity," + "-Infinity," + "Infinity"
    # print root_print
    f1.write(root_print)
    f1.write("\n")
    rec1(temp_list, root, f1)
    f1.close()
    x = sorted(root['children'], key=lambda l: (l['value'], l['x'], -l['y']), reverse=True)[0]
    x_cord = x['x']
    y_cord = x['y']
    # print x
    temp_list[x_cord][y_cord] = player
    # display(board)
    f = open("next_state.txt", "w")
    for a in range(0, int(board_size), 1):
        for b in range(0, int(board_size), 1):
            f.write(temp_list[a][b])
        f.write("\n")
    f.close()


c = 0
player2 = ""
# Creating 2d List
for line_no, item in enumerate(content):

    # Algorithm to use 1 -> Greedy, 2 -> MiniMax, 3 -> Alpha Beta
    if line_no == 0:
        task = int(item)
        # print task

    # Player 1 or 2
    if line_no == 1:
        player = item

        if player == '1':
            player = 'b'
        else:
            player = 'w'

        if player == "w":
            player2 = "b"
        else:
            player2 = "w"
            # print player

    # Depth of the tree to search
    if line_no == 2:
        cut_of_depth = int(item)
        # print cut_of_depth

    # Size of the board
    if line_no == 3:
        board_size = int(item)
        # print board_size

    # Reading the board state and generating a 2D list

    if line_no >= 4:
        list1.append([])
        temp_list.append([])
        for j, element in enumerate(item):  # j is the column number
            # list1[c].append(element)
            temp_list[c].append(element)
        c += 1

if task == 1:
    greedy(temp_list)
if task == 2:
    depth = 0
    ply1 = player
    ply2 = player2
    mini_max()
if task == 3:
    depth = 0
    ply1 = player
    ply2 = player2
    alpha_beta()
