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

pieces = {-1:"\u25CB",0:" ",1:"\u25CF"}

board = []
for i in range(8):
    board.append([])
    for j in range(8):
        board[i].append(0)

def Print():
    s = ""
    s += ' '*3
    for i in range(8):
        s += str(i+1) + ' '*3
    s += '\n' +" "+ ulcorner

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
    s += drcorner
    print(s)

board[3][3],board[4][4] = -1,-1
board[3][4],board[4][3] = 1,1


def move(p,a,check):
    global board
    px,py = p
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
    player = -1
    print('''
Rules
''')
    Print()
    print(pieces[player],'\'s turn: ')
    while True:
        flag = True                    
        if not checkValid(player):
            if not checkValid(player*-1):
                break
            else:
                print(pieces[player],"has no valid moves. Turn skipped")
                player*=-1
                    
        pos = [int(i) for i in input("Enter location: ").split(',')]
        pos[0],pos[1] = pos[0] - 1, pos[1] - 1
        pos = tuple(pos)
        if move(pos,player,False):
            Print()
        else:
            print("Not a Valid move")
            continue
            
        player *= -1
        print(pieces[player],'\'s turn: ')

Play()
