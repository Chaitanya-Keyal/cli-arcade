import time
import random
ulcorner = '┌'
drcorner = '┘'
hedge = '─'
urcorner = '┐'
dlcorner = '└'
dplus = '┬'
lplus = '┤'
vedge = '│'
plus =  '┼'
rplus = '├'
uplus = '┴'

pieces = {-1:"\u25CB",0:" ",1:"\u25CF"} #Symbol for the two colors
dcnt = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}

board = []

def Print():
    s = ""
    s += " "+ ulcorner

    for i in range(7):
        s += hedge*3 + dplus
    s += hedge*3 + urcorner + '\n'
        
    for i in range(8):
        s += str(i+1)
        for j in range(8):
            c = pieces[board[i][j]]
            s += vedge + ' ' + c +' '
        s += vedge + '\n'
        if i == 7:
            continue
        s += ' '
        s += rplus + hedge*3 
        for j in range(7):
            s += plus + hedge*3 
        s += lplus + '\n'
    s += ' ' + dlcorner + hedge*3 
    for j in range(7):
        s += uplus + hedge*3 
    s += drcorner + '\n'
    s += ' '*3
    for i in range(8):
        s += chr(ord('A')+i) + ' '*3
    print(s)
    print('-'*35)

def move(p,a,check):
    global board
    px,py = p
    if board[px][py] != 0:
        return False
    flag = False

    #Right
    for i in range(px+1,8):
        if i == px+1 and board[i][py] != -a:
            break
        elif board[i][py] == 0:
            break
        elif board[i][py] == a:
            flag = True
            if check:
                break
            for j in range(px,i+1):
                board[j][py] = a
            break

    #Left        
    for i in range(px-1,-1,-1):
        if i == px-1 and board[i][py] != -a:
            break
        elif board[i][py] == 0:
            break
        elif board[i][py] == a:
            flag = True
            if check:
                break
            for j in range(i,px+1):
                board[j][py] = a
            break
        
    #Top            
    for i in range(py+1,8):
        if i == py+1 and board[px][i] != -a:
            break
        elif board[px][i] == 0:
            break
        elif board[px][i] == a:
            flag = True
            if check:
                break
            for j in range(py,i+1):
                board[px][j] = a
            break
            
        
    #Bottom   
    for i in range(py-1,-1,-1):
        if i == py-1 and board[px][i] != -a:
            break
        elif board[px][i] == 0:
            break
        elif board[px][i] == a:
            flag = True
            if check:
                break
            for j in range(i,py+1):
                board[px][j] = a
            break
        
    #Top Right            
    for i, j in zip(range(px+1,8), range(py+1,8)):
        if i == px+1 and j == py+1 and board[i][j] != -a:
            break
        elif board[i][j] == 0:
            break
        elif board[i][j] == a:
            flag = True
            if check:
                break
            for i1, j1 in zip(range(px,i+1), range(py,j+1)):
                board[i1][j1] = a
            break
                
    #Top Left    
    for i, j in zip(range(px+1,8), range(py-1,-1,-1)):
        if i == px+1 and j == py-1 and board[i][j] != -a:
            break
        elif board[i][j] == 0:
            break
        elif board[i][j] == a:
            flag = True
            if check:
                break
            for i1, j1 in zip(range(px,i+1), range(py,j-1,-1)):
                board[i1][j1] = a
            break

    #Bottom Right
    for i, j in zip(range(px-1,-1,-1), range(py+1,8)):
        if i == px-1 and j == py+1 and board[i][j] != -a:
            break
        elif board[i][j] == 0:
            break
        elif board[i][j] == a:
            flag = True
            if check:
                break
            for i1, j1 in zip(range(px,i-1,-1), range(py,j+1)):
                board[i1][j1] = a
            break
        
    #Bottom Left
    for i, j in zip(range(px-1,-1,-1), range(py-1,-1,-1)):
        if i == px-1 and j == py-1 and board[i][j] != -a:
            break
        elif board[i][j] == 0:
            break
        elif board[i][j] == a:
            flag = True
            if check:
                break
            for i1, j1 in zip(range(px,i-1,-1), range(py,j-1,-1)):
                board[i1][j1] = a
            break

    return flag

def checkValid(player):
    for i in range(8):
        for j in range(8):
            if move((i,j),player,True):
                return True
    return False

def Play():

    #Initializing Board
    for i in range(8):
        board.append([])
        for j in range(8):
            board[i].append(0)
    board[3][3],board[4][4] = -1,-1
    board[3][4],board[4][3] = 1,1   

    print('''
Rules:
<Blah Blah>
You can chose any of the 3 modes:
1) Player vs Player
2) Player vs Computer
3) Computer vs Computer
    ''') #Option 3 is for observing if the code works without the hassle of giving 64 inputs 
    while True:
        try:
            a = int(input("Enter mode: "))
            if a > 3 or a < 1:
                raise Exception("NO")
            else:
                break
        except:
            print("Invalid Selection!")

    if a == 1:
        Multiplayer()
    elif a == 2:
        Singleplayer()
    elif a == 3:
        Auto()

def Multiplayer():
    player = -1
    Print()
    while True:
        if not checkValid(player):
            if not checkValid(player*-1):
                break
            else:
                print(pieces[player],"has no valid moves. Turn skipped")
                print()
                player*=-1

        while True:
            while True:
                try:
                    s = input(pieces[player]+'\'s move: ')
                    if len(s) != 2:
                        raise Exception("Invalid Length")
                    elif not (1<=int(s[1])<=8):
                        raise Exception('px Input Invalid')
                    else:
                        px = int(s[1]) - 1
                        py = dcnt[s[0].upper()] - 1
                    break
                except:
                    print("Invalid Input. Try again")
                    print()

            if move((px,py),player,False):
                #print(pieces[player],'played: %s%s' % (chr(ord('A')+py),px+1))
                print()
                Print()
                time.sleep(0.3)
                break
            else:
                print("Not a valid move(refer rules)")
                print()
                continue
        player *= -1
    End()

def Singleplayer():
    player = -1
    Print()
    while True:
        if not checkValid(player):
            if not checkValid(player*-1):
                break
            else:
                print(pieces[player],"has no valid moves. Turn skipped")
                print()
                player*=-1

        if player == 1:
            time.sleep(1)
            while True:
                px = random.randint(0,7)
                py = random.randint(0,7)
                if move((px,py),player,False):
                    print(pieces[player],'played: %s%s' % (chr(ord('A')+py),px+1))
                    print()
                    Print()
                    break
                else:
                    continue
            player *= -1
            continue

        while True:
            while True:
                try:
                    s = input(pieces[player]+'\'s move: ')
                    if len(s) != 2:
                        raise Exception("Invalid Length")
                    elif not (1<=int(s[1])<=8):
                        raise Exception('px Input Invalid')
                    else:
                        px = int(s[1]) - 1
                        py = dcnt[s[0].upper()] - 1
                    break
                except:
                    print("Invalid Input. Try again")
                    print()

            if move((px,py),player,False):
                #print(pieces[player],'played: %s%s' % (chr(ord('A')+py),px+1))
                print()
                Print()
                time.sleep(0.3)
                break
            else:
                print("Not a valid move(refer rules)")
                print()
                continue
        player *= -1
    End()

def Auto():
    while True:
        try:
            sleep = int(input("Enter time(in ms) to wait between each move: ")) / 1000
            break
        except:
            print("Invalid time")

    player = -1
    Print()
    while True:
        if not checkValid(player):
            if not checkValid(player*-1):
                break
            else:
                print(pieces[player],"has no valid moves. Turn skipped")
                print()
                player*=-1

        while True:
            px = random.randint(0,7)
            py = random.randint(0,7)
            if move((px,py),player,False):
                print(pieces[player],'played: %s%s' % (chr(ord('A')+py),px+1))
                print()
                Print()
                time.sleep(sleep)
                break
            else:
                continue
        player *= -1
    End()
    
def End():
    p1 = 0
    p2 = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                p1 += 1
            elif board[i][j] == -1:
                p2 += 1

    if (p1+p2) != 64 == 0:
        print("Game Ended- No Valid Moves left")
    else:
        print("Game Ended - Board Filled")
    if p1 > p2:
        print(pieces[1],'won the game')
    elif p2 > p1:
        print(pieces[-1],'won the game')
    else:
        print("Draw")
    print()
    print(pieces[1],'-',p1)
    print(pieces[-1],'-',p2)

Play()
