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
    print(' '*3,end='')
    for i in range(8):
        print((i+1),' '*3,sep='',end='')
    print()
    print('',ulcorner,end = '')
    
    for i in range(7):
        print(hedge*3,dplus,sep='',end='')
    print(hedge*3,urcorner,sep='')
    
    for i in range(8):
        print(i+1,end='')
        for j in range(8):
            c = pieces[board[i][j]]
            print(vedge,' ',c,' ',end='',sep='')
        print(vedge)
        if i == 7:
            continue
        print(' ',end='')
        print(rplus,hedge*3,end='',sep='')
        for j in range(7):
            print(plus,hedge*3,end='',sep='')
        print(lplus)
    print(' ',end='')
    print(dlcorner,hedge*3,end='',sep='')
    for j in range(7):
        print(uplus,hedge*3,end='',sep='')
    print(drcorner)

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


