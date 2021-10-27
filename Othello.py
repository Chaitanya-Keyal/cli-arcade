def Othello():
    ulcorner = '┌'
    drcorner = '┘'
    urcorner = '┐'
    dlcorner = '└'
    hedge = '─'
    vedge = '│'
    dplus = '┬'
    uplus = '┴'
    lplus = '┤'
    rplus = '├'
    plus = '┼'
    
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

    
    def isValid(p,a):
        px,py = p
        for i in range(8):
            if board[px][i] == a:
                pass
        
    

Othello()
