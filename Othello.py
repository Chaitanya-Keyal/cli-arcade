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

pieces = {-1:"O",0:" ",1:"X"}
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


def move(p,a):
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
            for j in range(px+1,i):
                board[j][py] = a

    #Left        
    for i in range(px-1,-1,-1):
        if i == px-1 and board[i][py] != -a:
            break
        elif board[i][py] == 0:
            break
        elif board[i][py] == a:
            flag = True
            for j in range(i,px):
                board[j][py] = a
    #Top            
    for i in range(py+1,8):
        if i == py+1 and board[px][i] != -a:
            break
        elif board[px][i] == 0:
            break
        elif board[px][i] == a:
            flag = True
            for j in range(py+1,i):
                board[px][j] = a
            
        
    #Bottom   
    for i in range(py-1,-1,-1):
        if i == py-1 and board[px][i] != -a:
            break
        elif board[px][i] == 0:
            break
        elif board[px][i] == a:
            flag = True
            for j in range(i,py):
                board[px][j] = a
    #Top Right            
    for i, j in zip(range(px+1,8), range(py+1,8)):
        if i == px+1 and j == py+1 and board[i][j] != -a:
            break
        elif board[i][j] == 0:
            break
        elif board[i][j] == a:
            flag = True
            for i1, j1 in zip(range(px+1,i), range(py+1,j)):
                board[i1][j1] = a
                
    #Top Left    
    for i, j in zip(range(px+1,8), range(py-1,-1,-1)):
        if i == px+1 and j == py-1 and board[i][j] != -a:
            break
        elif board[i][j] == 0:
            break
        elif board[i][j] == a:
            flag = True
            for i1, j1 in zip(range(px+1,i), range(py-1,j,-1)):
                board[i1][j1] = a

    #Bottom Right
    for i, j in zip(range(px-1,-1,-1), range(py+1,8)):
        if i == px-1 and j == py+1 and board[i][j] != -a:
            break
        elif board[i][j] == 0:
            break
        elif board[i][j] == a:
            flag = True
            for i1, j1 in zip(range(px-1,i,-1), range(py+1,j)):
                board[i1][j1] = a
    #Bottom Left
    for i, j in zip(range(px-1,-1,-1), range(py-1,-1,-1)):
        if i == px-1 and j == py-1 and board[i][j] != -a:
            break
        elif board[i][j] == 0:
            break
        elif board[i][j] == a:
            flag = True
            for i1, j1 in zip(range(px-1,i,-1), range(py-1,j,-1)):
                board[i1][j1] = a

    return flag
Print()
