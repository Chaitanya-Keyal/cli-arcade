import random
import os
import sys
import time
import copy

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
player = 0
pieces = {-1:"\u25CB",0:" ",1:"\u25CF"} #Symbol for the two colors
dcnt = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}

board = []
marker = []

def slowprint(s,t=0.025):
    for i in s:
        print(i,end='')
        if isIDLE():
            time.sleep(t)

def isIDLE():
   if "idlelib" in sys.modules:
      return True
   else:
      return False

def newscreen(n=105,t=0.6):
    print("\nLoading",end='')
    for i in range(3):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(t)
    print()
    if isIDLE():
        print('-'*n)
    else:
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')

def Print(copy,st = False):
    def Line(line):
        space = 8
        if line == 0:
            s = ""
            s += " "+ ulcorner
            s += (hedge*3 + dplus)*7 + hedge*3 + urcorner
            if st:
                return s
            s += ' '*space
            s += " "+ ulcorner
            s += (hedge*3 + dplus)*7 + hedge*3 + urcorner
            return s
            
        elif line == 16:
            s = ' '
            s += dlcorner + hedge*3 + (uplus + hedge*3)*7 + drcorner
            if st:
                return s
            s += ' '*space + ' '
            s += dlcorner + hedge*3 + (uplus + hedge*3)*7 + drcorner
            return s

        elif line == 17:
            s = '   '
            for i in range(8):
                s += chr(ord('A')+i) + ' '*3
            if st:
                return s
            s += ' '*space + '  '
            for i in range(8):
                s += chr(ord('A')+i) + ' '*3
            return s

        elif line % 2 == 1:
            s = ""
            i = (line - 1)//2
            s += str(i+1)

            if not st:
                for j in range(8):
                    c = pieces[copy[i][j]]
                    if marker[i][j] == 1:
                        s += vedge + '<' + c +'>'  #Flipped Piece Indicator
                    elif marker[i][j] == 2:
                        s += vedge + '[' + c +']'
                    elif marker[i][j] == 3:
                        s += vedge + '(' + pieces[board[i][j]] +')'
                    else:
                        s += vedge + ' ' + c +' '

                s += vedge 
                if line == 7 or line == 9:
                    s += ' '*(space//2 - 1) + '→'*1 + ' '*(space//2 )
                else:
                    s += ' '*space
                s += str(i+1)

            for j in range(8):
                c = pieces[board[i][j]]
                s += vedge + ' ' + c +' '
            s += vedge 
            return s

        elif line %2 == 0:
            s = ' '
            s += rplus + hedge*3 + (plus + hedge*3)*7 + lplus
            if st:
                return s

            if line == 8:
                s += ' '*(space//2 - 1) + '→'*1 + ' '*(space//2 )
            else:
                s += ' '*space
            s += ' '
            s += rplus + hedge*3 + (plus + hedge*3)*7 + lplus
            return s
    
    b = ''
    for i in range(18):
        b += Line(i) + '\n'
    print(b)
    print('-'*80)

def move(p,a,check):
    global board,marker
    px,py = p
    if board[px][py] != 0:
        return False
    for i in range(8):
        for j in range(8):
            marker[i][j] = 0
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
                marker[j][py] = 1
                board[j][py] = a
            marker[i][py] = 2
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
                marker[j][py] = 1
                board[j][py] = a
            marker[i][py] = 2
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
                marker[px][j] = 1
                board[px][j] = a
            marker[px][i] = 2
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
                marker[px][j] = 1
                board[px][j] = a
            marker[px][i] = 2
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
                marker[i1][j1] = 1
                board[i1][j1] = a
            marker[i][j] = 2
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
                marker[i1][j1] = 1
                board[i1][j1] = a
            marker[i][j] = 2
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
                marker[i1][j1] = 1
                board[i1][j1] = a
            marker[i][j] = 2
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
                marker[i1][j1] = 1
                board[i1][j1] = a
            marker[i][j] = 2
            break
    if flag:
        marker[px][py] = 3       
    return flag

def checkValid(player):
    for i in range(8):
        for j in range(8):
            if move((i,j),player,True):
                return True
    return False

def Play():
    #Initializing Board
    global board,marker
    board = []
    marker = []
    for i in range(8):
        board.append([])
        marker.append([])
        for j in range(8):
            board[i].append(0)
            marker[i].append(0)

    board[3][3],board[4][4] = -1,-1
    board[3][4],board[4][3] = 1,1   

    print('''Rules:
1. The board will start with 2 black discs and 2 white discs at the centre of the board.
2. The goal is to get the majority of colour discs on the board at the end of the game.
3. One player plays black and the other white.
4. Then the game alternates between white and black until:
    i.  One player can not make a valid move to outflank the opponent.
    ii. Both players have no valid moves.
            *When a player has no valid moves, the turn is passed and the opponent continues.
5. When both players have no valid moves, the game ends.
6. The discs are counted and the player with the majority of their colour discs wins.
''')
    print('''Input Rules:
1. Each move played HAS to "out-flank" at least one of the opponent's discs.
   i.e. At least one of the opponent's disc has to get flipped
2. A disc or row of discs is outflanked when it is surrounded at the ends by discs of the opposite color.
3. A disc may outflank any number of discs in one or more rows in any direction (horizontal, vertical, diagonal).
4. All the discs which are outflanked, i.e. surrounded by opposite colors at each end of the row, will be flipped.

5. Enter Input in the form - <Alphabet><Number>
   E.g. A1, C3, b4, g8
''')
    slowprint('''You can chose any of the 3 modes:
1) Player vs Player
2) Player vs Computer
3) Computer vs Computer

''',t=0.02)
#Option 3 is for observing if the code works without the hassle of giving 64 inputs 
    while True:
        try:
            a = int(input("Enter mode: "))
            if a > 3 or a < 1:
                raise Exception("NO")
            else:
                break
        except:
            print('-'*45)
            slowprint("ERROR")
            print("\n\nInvalid Selection! (Enter 1, 2 or 3)")
            print('-'*45)
            time.sleep(1)

    print('-'*80)
    if a == 1:
        Multiplayer()
    elif a == 2:
        Singleplayer()
    elif a == 3:
        Auto()

def Multiplayer():
    player = -1
    Player = 1
    Print(board,True)
    while True:
        if player == -1:
            Player = 1
        else:
            Player = 2
        if not checkValid(player):
            if not checkValid(player*-1):
                break
            else:
                print('Player %s (%s) has no valid moves. Turn skipped' % (str(Player),pieces[player]))
                print()
                player*=-1
                Player = Player%2 + 1

        while True:
            while True:
                try:
                    s = input('Player %s\'s (%s) move: ' % (str(Player),pieces[player]))
                    if len(s) != 2:
                        raise Exception("Invalid Length")
                    elif not (1<=int(s[1])<=8):
                        raise Exception('px Input Invalid')
                    else:
                        px = int(s[1]) - 1
                        py = dcnt[s[0].upper()] - 1
                    break
                except:
                    print('-'*60)
                    slowprint("ERROR")
                    print('''

Invalid Input! Enter Input in the form - <Alphabet><Number>
               E.g. A1, C3, b4, g8
''')
                    print('-'*60)
                    time.sleep(1)
                    
            lcopy = copy.deepcopy(board)
            if move((px,py),player,False):
                #print(pieces[player],'played: %s%s' % (chr(ord('A')+py),px+1))
                print()
                newscreen(n = 80, t = 0.15)
                Print(lcopy)
                break
            else:
                print('-'*115)
                slowprint("ERROR")
                print('''

Not a Valid Move!

Input Rules:
1. Each move played HAS to "out-flank" at least one of the opponent's discs.
   i.e. At least one of the opponent's disc has to get flipped
2. A disc or row of discs is outflanked when it is surrounded at the ends by discs of the opposite color.
3. A disc may outflank any number of discs in one or more rows in any direction (horizontal, vertical, diagonal).
4. All the discs which are outflanked, i.e. surrounded by opposite colors at each end of the row, will be flipped. 
''')
                print('-'*115)
                time.sleep(1)
                continue
        player *= -1
    End("Player 1","Player 2")

def Singleplayer():
    player = -1
    Player = 'Player'
    Print(board,True)
    while True:
        if player == -1:
            Player = 'Player'
        else:
            Player = 'Computer'
        if not checkValid(player):
            if not checkValid(player*-1):
                break
            else:
                print("%s(%s) has no valid moves. Turn skipped" % (Player,pieces[player]))
                print()
                player*=-1
                if player == -1:
                    Player = 'Player'
                else:
                    Player = 'Computer'

        if player == 1:
            time.sleep(1)
            while True:
                px = random.randint(0,7)
                py = random.randint(0,7)
                lcopy = copy.deepcopy(board)
                if move((px,py),player,False):
                    print('%s (%s) played: %s%s' % (Player,pieces[player],chr(ord('A')+py),px+1))
                    print()
                    newscreen(n = 80, t = 0.15)
                    Print(lcopy)
                    break
                else:
                    continue
            player *= -1
            continue

        while True:
            while True:
                try:
                    s = input('%s\'s (%s) move: ' % (Player,pieces[player]))
                    if len(s) != 2:
                        raise Exception("Invalid Length")
                    elif not (1<=int(s[1])<=8):
                        raise Exception('px Input Invalid')
                    else:
                        px = int(s[1]) - 1
                        py = dcnt[s[0].upper()] - 1
                    break
                except:
                    print('-'*60)
                    slowprint("ERROR")
                    print('''

Invalid Input! Enter Input in the form - <Alphabet><Number>
               E.g. A1, C3, b4, g8
''')
                    print('-'*60)
                    time.sleep(1)
                    
            lcopy = copy.deepcopy(board)
            if move((px,py),player,False):
                #print(pieces[player],'played: %s%s' % (chr(ord('A')+py),px+1))
                print()
                newscreen(n = 80, t = 0.15)
                Print(lcopy)
                break
            else:
                print('-'*115)
                slowprint("ERROR")
                print('''

Not a Valid Move!

Input Rules:
1. Each move played HAS to "out-flank" at least one of the opponent's discs.
   i.e. At least one of the opponent's disc has to get flipped
2. A disc or row of discs is outflanked when it is surrounded at the ends by discs of the opposite color.
3. A disc may outflank any number of discs in one or more rows in any direction (horizontal, vertical, diagonal).
4. All the discs which are outflanked, i.e. surrounded by opposite colors at each end of the row, will be flipped. 
''')
                print('-'*115)
                time.sleep(1)
                continue
        player *= -1
    End("Player","Computer")

def Auto():
    while True:
        try:
            sleep = int(input("Enter time (in ms) to wait between each move: ")) / 100
            if sleep<0:
                raise Exception("NegativeTime")
            break
        except NegativeTime:
            print('-'*45)
            slowprint("ERROR")
            print("\n\nInvalid Time! Time has to be positive!")
            print('-'*45)
            time.sleep(1)
        except:
            print('-'*45)
            slowprint("ERROR")
            print("\n\nInvalid Time! Enter digits only!")
            print('-'*45)
            time.sleep(1)

    player = -1
    Player = 1
    Print(board,True)
    while True:
        if player == -1:
            Player = 1
        else:
            Player = 2

        if not checkValid(player):
            if not checkValid(player*-1):
                break
            else:
                print('Bot %s (%s) has no valid moves. Turn skipped' % (str(Player),pieces[player]))
                print()
                player*=-1
                Player = Player%2 + 1

        while True:
            px = random.randint(0,7)
            py = random.randint(0,7)
            lcopy = copy.deepcopy(board)
            if move((px,py),player,False):
                print('Bot %s (%s) played: %s%s' % (str(Player),pieces[player],chr(ord('A')+py),px+1))
                print()
                newscreen(n = 80, t = (sleep/3))
                Print(lcopy)
                break
            else:
                continue
        player *= -1
    End("Bot 1","Bot 2")

def End(e1,e2):
    p1 = 0
    p2 = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                p1 += 1
            elif board[i][j] == -1:
                p2 += 1

    newscreen(n = 80, t = 0.15)

    if (p1+p2) != 64 == 0:
        print("Game Ended- No Valid Moves left")
    else:
        print("Game Ended - Board Filled")
    if p1 > p2:
        print( e2,'(%s) won the game' % pieces[1])
    elif p2 > p1:
        print(e1,'(%s) won the game' % pieces[-1])
    else:
        print("Draw")
    print()
    print( e1,'(%s) - %s' % (pieces[-1],str(p2)))
    print( e2,'(%s) - %s' % (pieces[1],str(p1)))
    print()
    for i in range(8):
        for j in range(8):
            marker[i][j] = 0

    Print(board,True)

ynl = ['y','ye','yes','yep','yup','yeah','yas','yass','yasss','yee',
       'n','no','nope','na','nah']

def PlayGame():
    slowprint("Welcome to Othello!\n",0.02)
    print('-'*80)
    while True:
        Play()
        while True:
            slowprint("Do you want to play Othello again? (y/n): ")
            f = input().lower().strip()
            if f in ynl:
                break
            else:
                slowprint("\nERROR\n\n")      
        if f in ynl[:10]:
            newscreen()
            continue
        else:
            newscreen()
            print("Thank you for playing Othello!\nGame created by: Pramit Pal")
            print('-'*35)
            newscreen(n=35,t=1.5)
            break
