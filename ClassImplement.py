import random
import os
import sys
import time
import copy

def slowprint(s,t=0.035):
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

class Othello:
    
    player = 0
    pieces = {-1:"\u25CB",0:" ",1:"\u25CF"} #Symbol for the two colors
    dcnt = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}
    
    board = []
    marker = []
    
    def Print(self,copy):
        board,dcnt,pieces,marker = self.board,self.dcnt,self.pieces,self.marker
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
        line = 0
        ct = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] != 0:
                    ct += 1

        def Line(line):
            space = 8
            if line == 0:
                s = ""
                s += " "+ ulcorner
                s += (hedge*3 + dplus)*7 + hedge*3 + urcorner
                if ct == 4:
                    return s

                s += ' '*space
                s += " "+ ulcorner
                s += (hedge*3 + dplus)*7 + hedge*3 + urcorner
                return s
                
            elif line == 16:
                s = ' '
                s += dlcorner + hedge*3 + (uplus + hedge*3)*7 + drcorner
                if ct == 4:
                    return s
                s += ' '*space + ' '
                s += dlcorner + hedge*3 + (uplus + hedge*3)*7 + drcorner
                return s
    
            elif line == 17:
                s = '   '
                for i in range(8):
                    s += chr(ord('A')+i) + ' '*3
                if ct == 4:
                    return s
                s += ' '*space + '  '
                for i in range(8):
                    s += chr(ord('A')+i) + ' '*3
                return s
    
            elif line % 2 == 1:
                s = ""
                i = (line - 1)//2
                s += str(i+1)
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
                if ct == 4:
                    return s
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
                if ct == 4:
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
        print('-'*70)
    
    def move(self,p,a,check):
        board,marker = self.board,self.marker
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
    
    def checkValid(self,player):
        for i in range(8):
            for j in range(8):
                if self.move((i,j),player,True):
                    return True
        return False
    
    def Play(self):
        board,marker = self.board,self.marker
        #Initializing Board
        for i in range(8):
            board.append([])
            marker.append([])
            for j in range(8):
                board[i].append(0)
                marker[i].append(0)
        board[3][3],board[4][4] = -1,-1
        board[3][4],board[4][3] = 1,1   
    
        print('''
    Rules:
    Enter Input in the form - <Alphabet><Number>
    Eg: A1, C3, b4, g8
    
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
            self.Multiplayer()
        elif a == 2:
            self.Singleplayer()
        elif a == 3:
            self.Auto()
    
    def Multiplayer(self):
        self.Print(self.board)
        board,dcnt,pieces = self.board,self.dcnt,self.pieces
        player = -1
        Player = 1
        while True:
            if player == -1:
                Player = 1
            else:
                Player = 2
            if not self.checkValid(player):
                if not self.checkValid(player*-1):
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
                        print("Invalid Input. Try again")
                        print()
                lcopy = copy.deepcopy(board)
                if self.move((px,py),player,False):
                    #print(pieces[player],'played: %s%s' % (chr(ord('A')+py),px+1))
                    print()
                    self.Print(lcopy)
                    time.sleep(0.3)
                    break
                else:
                    print("Not a valid move(refer rules)")
                    print()
                    continue
            player *= -1
        self.End("Player 1","Player 2")
    
    def Singleplayer(self):
        self.Print(self.board)
        board,dcnt,pieces = self.board,self.dcnt,self.pieces
        player = -1
        Player = 'Player'
        while True:
            if player == -1:
                Player = 'Player'
            else:
                Player = 'Computer'
            if not self.checkValid(player):
                if not self.checkValid(player*-1):
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
                    if self.move((px,py),player,False):
                        print('%s (%s) played: %s%s' % (Player,pieces[player],chr(ord('A')+py),px+1))
                        print()
                        self.Print(lcopy)
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
                        print("Invalid Input. Try again")
                        print()
                lcopy = copy.deepcopy(board)
                if self.move((px,py),player,False):
                    #print(pieces[player],'played: %s%s' % (chr(ord('A')+py),px+1))
                    print()
                    self.Print(lcopy)
                    time.sleep(0.3)
                    break
                else:
                    print("Not a valid move(refer rules)")
                    print()
                    continue
            player *= -1
        self.End("Player","Computer")
    
    def Auto(self):
        self.Print(self.board)
        board,dcnt,pieces = self.board,self.dcnt,self.pieces
        while True:
            try:
                sleep = int(input("Enter time(in ms) to wait between each move: ")) / 1000
                break
            except:
                print("Invalid time")
    
        player = -1
        Player = 1
        while True:
            if player == -1:
                Player = 1
            else:
                Player = 2
    
            if not self.checkValid(player):
                if not self.checkValid(player*-1):
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
                if self.move((px,py),player,False):
                    print('Bot %s (%s) played: %s%s' % (str(Player),pieces[player],chr(ord('A')+py),px+1))
                    print()
                    self.Print(lcopy)
                    time.sleep(sleep)
                    break
                else:
                    continue
            player *= -1
        self.End("Bot 1","Bot 2")
    
    def End(self,e1,e2):
        board,dcnt,pieces = self.board,self.dcnt,self.pieces
        marker = self.marker
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
    
    ynl = ['y','ye','yes','yep','yup','yeah','yas','yass','yasss','yee',
           'n','no','nope','na','nah']
    
    def __init__(self):
        while True:
            self.Play()
            while True:
                print("Do you want to play Othello again? (y/n): ")
                f = input().lower().strip()
                if f in self.ynl:
                    break
                else:
                    print("\nERROR\n\n")      
            if f in self.ynl[:10]:
                newscreen()
                continue
            else:
                newscreen()
                print("Thank you for playing Othello!")
                time.sleep(5)
                break
   
class MasterMind:
    valid = []
    lvl = {1:7,2:8,3:9,4:10}
    levelname = {1:"Easy",2:"Medium",3:"Difficult",4:"Insane"}
    code,codedisp,valid,plist,alist,op,counter=[],[],[],[],[],'',0

    def createDict(self,l):
        d = {}
        for i in range(4):
           temp = []
           for j in range(4):
              if l[i]==l[j]:
                 temp.append(j)
           d[l[i]] = temp
        return d
    
    def leveldisplay(self):
         print('Level - ',self.levelname[op],'\nThe code can have the following digits:\n',valid,sep='')
         print('-'*105)
    
    
    def initialize(self):
        global code,codedisp,plist,alist,op,counter,valid
        code = []
        valid = []
        codedisp = ['X','X','X','X']
        plist = []
        alist = []
        op = ''
        for i in range(10):
            plist.append(['-','-','-','-'])
            alist.append(['-','-','-','-']) 
        counter = 0
    
    def getKey(self,v):
       for i,j in self.levelname.items():
          if j==v:
             return i
       return -1
    
    def coder(self):
        global code,op,valid
        choose = '''Choose your level:
    1 - Easy
    2 - Medium
    3 - Difficult
    4 - Insane
    
    Enter your choice: '''
        while True:
          if op=='':
             slowprint(choose)
          else:
             slowprint(choose,0.004)
          op = input()
          try:
             op = int(op)
          except:
             op = self.getKey(op.title())
          if op not in self.levelname:
             print('-'*45)
             slowprint("ERROR")
             print("\n\nInvalid Choice! (Enter 1, 2, 3 or 4)")
             print('-'*45)
             time.sleep(1)
          else:
             break
        valid = [i for i in range(1,self.lvl[op])]
        for i in range(4):
            code.append(random.choice(valid))
        print('-'*45)
        slowprint("The code has been generated! Start Cracking!\n")
    
    def board_rules(self):
        print('-'*105)            
        out = '┌───────┬─────┬─────┬─────┬─────┐\n'
        out += '│ Code: │'
        
        for i in codedisp:
            out += '  '+str(i)+'  │'
            
        out += '\tRules of the game:\n'
        out += '├───────┼─────┼─────┼─────┼─────┤\n'
        
        for i in range(1,11):
            
              out += '│ '+str(plist[-i][0])+'   '+ str(plist[-i][1])+' │     │     │     │     │'
              if i==1:
                  out+= "\t1. Crack the 4 digit code (X X X X) generated by the computer.\n" 
              elif i==3:
                  out+= "\t\tXXXX\n" 
              elif i==4:
                  out+= "\t   the board, indicated by 2 pegs:\n" 
              elif i==5:
                  out+= "\t\t\tFor every correct digit that is\n"
              elif i==6:
                  out+= "\t\tii. Red Peg (R) -\n"
              else:
                  out+='\n'
                  
              out+= '│ '+str(plist[-i][2])+'   '+ str(plist[-i][3])+' │'
              
              for j in range(4):
                  out+= '  '+str(alist[-i][j])+'  │'
              if i==2:
                  out+= "\t3. The attempts can be entered in any of the following formats:\n"
              elif i==5:
                  out+= "\t\t\tplaced in the wrong position.\n"
              elif i==6:
                  out+= "\t\t\tFor every correct digit that is\n"
              elif i==7:
                  out+= "\t5. The order of these pegs does NOT matter.\n"
              else:
                  out+='\n'
    
              if i==10:
                  out+='└───────┴─────┴─────┴─────┴─────┘\n'
              else:
                  out+='├───────┼─────┼─────┼─────┼─────┤'
                  if i==1:
                      out+= "\t2. Digits may or may not be be repeated.\n"
                  elif i==2:
                      out+= "\t\tX X X X\n"
                  elif i==3:
                      out+= "\t4. After every attempt, clues will be given on the left side of\n"
                  elif i==4:
                      out+= "\t\ti.  White Peg (W) -\n"
                  elif i==6:
                      out+= "\t\t\tplaced in the correct position as well.\n"
                  else:
                      out+='\n'
        print(out)
        print('-'*105)
    
    def board(self):
        print('-'*105)    
        out = ('┌───────┬─────┬─────┬─────┬─────┐\n')
        out+=('│ Code: │')
        for i in codedisp:
            out+=('  '+str(i)+'  │')
        out+=('\n├───────┼─────┼─────┼─────┼─────┤\n')
        for i in range(1,11):   
              out += ('│ '+str(plist[-i][0])+'   '+ str(plist[-i][1])+' │     │     │     │     │\n') 
              out+=('│ '+str(plist[-i][2])+'   '+ str(plist[-i][3])+' │')    
              for j in range(4):
                  out+=('  '+str(alist[-i][j])+'  │')
              out += '\n'
              if i==10:
                  out+=('└───────┴─────┴─────┴─────┴─────┘\n')
              else:
                  out+=('├───────┼─────┼─────┼─────┼─────┤\n')
        print(out)
        print('-'*105)
        
    def breaker(self):
        global alist, plist
        pegs = []
        while True:
            slowprint("\nYour Attempt: ",0.02)
            ip = input()
            temp = []
            try:
               for i in ip:
                  if i.isspace():
                     continue
                  elif int(i) in [i for i in range(10)]:
                     temp.append(int(i))
            except:
               print('-'*105)
               slowprint("ERROR")
               print("\n\nInvalid Attempt! Please enter digits only!")
               print('-'*105)
               time.sleep(1)
               continue
            if len(temp) != 4:
               print('-'*105)
               slowprint("ERROR")
               print("\n\nInvalid Attempt! Please enter exactly 4 digits!")
               print('-'*105)
               time.sleep(1)
               continue
            attempt = []
            for i in temp:
               if i in valid:
                  attempt.append(i)
               else:
                  break
            if len(attempt) != 4:
               print('-'*105)
               slowprint("ERROR")
               print("\n\nInvalid Attempt! Please enter valid digits according to level!")
               print('-'*105)
               self.leveldisplay()
               time.sleep(1)
               continue
            else:
                alist[counter-1]=attempt
                break
       
        attemptdict = self.createDict(attempt)
        codedict = self.createDict(code)
        pegsd = {}
    
        for i,j in codedict.items():
              temp = []
              if i in attemptdict.keys():
                 for a in j:
                    if temp.count('R') != len(j):
                       if a in attemptdict[i]:
                             temp.append('R')
                       else:
                          if temp.count('W') != len(attemptdict[i]):
                             temp.append('W')
                 pegsd[i] = sorted(temp)[:len(attemptdict[i])]
    
        for i in pegsd.values():
              pegs.extend(i)
    
        random.shuffle(pegs)
          
        while len(pegs) != 4:
              pegs.insert(0,'-')
              
        plist[counter-1]=pegs
    
    def play(self):
        global codedisp,counter
        self.coder()
        while True:
            if code in alist or counter==10:
                newscreen()
                codedisp = code
                self.board()
                if code in alist:
                   slowprint("Congratulations!\nYou cracked the code in only "+str(counter)+" attempts!\n")
                else:
                   slowprint("Sorry, you have lost!\nThe correct code is displayed on the board!\n")
                newscreen(t=2.5)
                break
            counter+=1
            newscreen()
            self.board_rules()
            self.leveldisplay()
            slowprint("Attempt "+str(counter)+":\n")
            self.breaker()
    
    ynl = ['y','ye','yes','yep','yup','yeah','yas','yass','yasss','yee',
           'n','no','nope','na','nah']
    
    
    def __init__(self):

       slowprint('Welcome to MasterMind, The classic code-cracking game!\n',0.02)
       print('-'*105)
       slowprint('''1. The code-maker (Computer) will generate a 4 digit code (X X X X) based on the chosen level.
    2. The code-breaker (You) has to break this code,
       by duplicating its exact digits and positions.
    3. After every attempt,
       clues will be given on the left side of the board, indicated by 2 pegs:
    \ti.  White Peg (W) - For every correct digit that is placed in the wrong position.
    \tii. Red Peg (R)   - For every correct digit that is placed in the correct position as well.
    4. A total of 10 attempts are allowed before the game is over, and the code is revealed.
    5. The Aim of the game is to break the code with the least attempts.
    ''')
       print('-'*105)
       
       while True:
           self.initialize()
           self.play()
           while True:
               slowprint("Do you want to play MasterMind again? (y/n): ")
               f = input().lower().strip()
               if f in self.ynl:
                   break
               else:
                   slowprint("\nERROR\n\n")      
           if f in self.ynl[:10]:
               newscreen()
               continue
           else:
               newscreen()
               print("Thank you for playing MasterMind!\nGame created by: Chaitanya Keyal")
               time.sleep(5)
               break
             
class TicTacToe:

    def __init__(self):
        global drawboard
        global type_
        global Game
        
        self.welcomeTXT()
        print('\t\t\t\t\t\t\t\t\t\t\t\t',"="*22,sep='')
        
        self.loadingTXT()
    
        Game = 'Running'
        drawboard = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        type_=input("Do you want to play singleplayer or 1v1 : ").strip().lower()
        
        while True:
            if type_ not in ['singleplayer','1v1']:
                type_=input("\nPlease enter 'Singleplayer' for versing the computer ; Enter '1v1' to play against your friend : ").strip().lower()
                print()
            else:
                break
        if type_ == 'singleplayer':
            print("\n\n","-"*200,'\n',sep='')
            self.vsComputer()        
        else:
             print("\n\n","-"*200,'\n',sep='')
             self.vs1()
             
        self.again()
                    
    
    def welcomeTXT(self):
        print("\t\t\t\t\t\t\t\t\t\t\t\t",end='')
        st= "Welcome to Tic-Tac-Toe"
        for i in st:
            print(i,end='')
            time.sleep(.10)
        print()
    
    
    def vs1(self):   
        self.rulesTXT()
        self.loadingTXT()
        print("\n\n","-"*200,'\n',sep='')
        print('Let the games begin!!!\n')
        print("","-"*200,'\n',sep='')
        print("\nPlayer 1 [X] --- Player 2 [O]\n")
        time.sleep(1)
        print()
        self.mainGame_code_vs1()   
        self.tyTXT()
        
        
    
    def vsComputer(self):
        global firstmark
        global secondmark
        self.rulesTXT()
        self.loadingTXT()
        self.difficulty_choice()
        self.loadingTXT()
        firstmark = input("What do you want to play as : ").upper().strip()
        while True:
           
            if firstmark not in ['O','X']:
                firstmark = input("Please enter a valid symbol :").upper().strip()
            else:
                break
    
        if firstmark == 'O':
            secondmark = 'X'
        else:
            secondmark = 'O'
    
        print("\n\n","-"*200,'\n',sep='')    
        print("\nPlayer [",firstmark,"] --- Computer [",secondmark,"]\n")
        self.loadingTXT()
        print("","-"*200,'\n',sep='')  
        print('Let the games begin!!!\n\n')
        
        self.mainGame_code_CVP()
        
        self.tyTXT()  
        
            
    
    
    #Displays the rules of the game
    def rulesTXT(self):
        if type_ == '1v1':
            st='''
    RULES FOR TIC-TAC-TOE (1v1) :-
    
      1. The game is played on a grid that's 3 squares by 3 squares.
    
      2. You are X, your friend is O. Players take turns putting their marks in empty squares.
    
      3. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
    
      4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.'''
    
            for i in st:
                print(i,end='')
                time.sleep(.035)
        else:
               st='''
    RULES FOR TIC-TAC-TOE (Singleplayer) :-
    
      1. The game is played on a grid that's 3 squares by 3 squares.
    
      2. Assume that you are X and the computer is O. Players take turns putting their marks in empty squares.
    
      3. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
    
      4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.'''
    
               for i in st:
                   print(i,end='')
                   time.sleep(.035)
                   
        print("\n\n\n","-"*200,'\n',sep='')
            
    #Loading text
    def loadingTXT(self):    
        print("\nLoading, Please Wait ",end='')
        for i in range(5):
            print("." , end=" ")
            time.sleep(1)
        print()
        print()
        print()
    
    
    def difficulty_choice(self):
        global diff
        diff = input("Do you wish to play at easy or hard difficulty : ").lower().strip()
        while True:        
            if diff not in ['easy','hard']:
                diff = input("Please enter 'easy' for easy difficulty and 'hard' for hard difficulty... : ").lower().strip()
            else:
                break
        print("\n\n","-"*200,'\n',sep='')
    
    
    def mainGame_code_vs1(self):
        global player    
        player = 1
        Game = 'Running'
        print("-"*200,'\n',sep='')
        print("\nThe empty board : \n")
        while(Game == 'Running'):
            
            self.Disp_Board()
            print("\n\n","-"*200,'\n',sep='')     
       
            if(player % 2 != 0):    
                print("\nPlayer 1's chance")    
                Symbol = 'X'    
            else:    
                print("\nPlayer 2's chance")    
                Symbol = 'O'
            cho = int(input("Enter the position between [1-9] where you want to mark : "))
            print()
            if 1<=cho<=9:
                if(self.Position_Check(cho)):    
                   player,Game=self.ext(cho,player,Symbol)
                else:
                    while True:
                        cho = int(input("\nAlready entered. Enter different position : "))
                        print()
                        if self.Position_Check(cho):                   
                            player,Game=self.ext(cho,player,Symbol)
                            break
            else:
                while True:
                        cho = int(input("\nPlease enter a position beteen 1 and 9 : "))
                        print()
                        if self.Position_Check(cho):
                             player,Game=self.ext(cho,player,Symbol)
                             break
        self.Disp_Board()    
        if(Game=='Draw'):    
            prtst="\nGame Draw..."
            for i in prtst:
                    print(i,end='')
                    time.sleep(.035)
        elif(Game=='Win'):    
            player-=1    
            if(player%2!=0):    
                prtst="\nCongrats! You defeated the player 2 and won the game!!"
                for i in prtst:
                    print(i,end='')
                    time.sleep(.035)
            else:    
                prtst="\nCongrats! You defeated the player 1 and won the game!!"
                for i in prtst:
                    print(i,end='')
                    time.sleep(.035) 
    
    
    def Disp_Board(self):    
        print(" %c | %c | %c " % (drawboard[1],drawboard[2],drawboard[3]))    
        print("___|___|___")    
        print(" %c | %c | %c " % (drawboard[4],drawboard[5],drawboard[6]))    
        print("___|___|___")    
        print(" %c | %c | %c " % (drawboard[7],drawboard[8],drawboard[9]))    
        print("   |   |   ")
    
    
    def Position_Check(self,x):    
        if(drawboard[x] == ' '):    
            return True    
        else:    
            return False
    
    def Game_Win_vs1(self):    
           # global Game
            
            #Horizontal winning condition
            
            if(drawboard[1] == drawboard[2] and drawboard[2] == drawboard[3] and drawboard[1] != ' '):    
                Game = 'Win'    
            elif(drawboard[4] == drawboard[5] and drawboard[5] == drawboard[6] and drawboard[4] != ' '):    
                Game = 'Win'    
            elif(drawboard[7] == drawboard[8] and drawboard[8] == drawboard[9] and drawboard[7] != ' '):    
                Game = 'Win'
                
            #Vertical Winning Condition
                
            elif(drawboard[1] == drawboard[4] and drawboard[4] == drawboard[7] and drawboard[1] != ' '):    
                Game = 'Win'    
            elif(drawboard[2] == drawboard[5] and drawboard[5] == drawboard[8] and drawboard[2] != ' '):    
                Game = 'Win'    
            elif(drawboard[3] == drawboard[6] and drawboard[6] == drawboard[9] and drawboard[3] != ' '):    
                Game = 'Win'
                
            #Diagonal Winning Condition
                
            elif(drawboard[1] == drawboard[5] and drawboard[5] == drawboard[9] and drawboard[5] != ' '):    
                Game = 'Win'    
            elif(drawboard[3] == drawboard[5] and drawboard[5] == drawboard[7] and drawboard[5] != ' '):    
                Game='Win'
                
            #Match Tie or Draw Condition
                
            elif(drawboard[1]!=' ' and drawboard[2]!=' ' and drawboard[3]!=' ' and drawboard[4]!=' ' and drawboard[5]!=' ' and drawboard[6]!=' ' and drawboard[7]!=' ' and drawboard[8]!=' ' and drawboard[9]!=' '):    
                Game='Draw'    
            else:            
                Game='Running'
    
            return Game
    
    
    def Emp_Pos(self,x):
        l=[]
        for i in range(1,len(drawboard)):
            if(drawboard[i] == ' '):    
                 l.append(i)
        return l
    
    
    def easy(self):       
            selection = self.Emp_Pos(drawboard)
            current_loc = random.choice(selection)
            drawboard[current_loc] = secondmark
    
    def hard(self):
            
            if(drawboard[1] == drawboard[2] and drawboard[3]==' ' and drawboard[1] == secondmark):
                drawboard[3]=secondmark
                
            elif(drawboard[2] == drawboard[3] and drawboard[1]==' ' and drawboard[3] == secondmark):
                drawboard[1]=secondmark
                
            elif(drawboard[1] == drawboard[3] and drawboard[2]==' ' and drawboard[1] == secondmark):    
                drawboard[2]=secondmark
                
            elif(drawboard[4] == drawboard[5] and drawboard[6]==' ' and drawboard[4] == secondmark):
                 drawboard[6]=secondmark
                 
            elif(drawboard[5] == drawboard[6] and drawboard[4]==' ' and drawboard[5] == secondmark):
                drawboard[4]=secondmark
                
            elif(drawboard[4] == drawboard[6] and drawboard[5]==' ' and drawboard[4] == secondmark):
                drawboard[5]=secondmark
                
            elif(drawboard[7] == drawboard[8] and drawboard[9]==' ' and drawboard[7] == secondmark):
                drawboard[9]=secondmark
                
            elif(drawboard[8] == drawboard[9] and drawboard[7]==' ' and drawboard[8] == secondmark):
                drawboard[7] = secondmark
                
            elif(drawboard[7] == drawboard[9] and drawboard[8]==' ' and drawboard[9] == secondmark):
                drawboard[8]=secondmark
                
                
            elif(drawboard[1] == drawboard[4] and drawboard[7]==' ' and drawboard[1] == secondmark):
                drawboard[7] = secondmark
                
            elif(drawboard[4] == drawboard[7] and drawboard[1]==' ' and drawboard[4] == secondmark):
                drawboard[1] = secondmark
                
            elif(drawboard[1] == drawboard[7] and drawboard[4]==' ' and drawboard[1] == secondmark):
                drawboard[4] = secondmark
                
            elif(drawboard[2] == drawboard[5] and drawboard[8]==' ' and drawboard[2] == secondmark):
                drawboard[8] = secondmark
                
            elif(drawboard[5] == drawboard[8] and drawboard[2]==' ' and drawboard[5] == secondmark):
                drawboard[2] = secondmark
                
            elif(drawboard[2] == drawboard[8] and drawboard[5]==' ' and drawboard[2] == secondmark):
                drawboard[5] = secondmark
                
            elif(drawboard[3] == drawboard[6] and drawboard[9]==' ' and drawboard[3] == secondmark):
                drawboard[9] = secondmark
                
            elif(drawboard[6] == drawboard[9] and drawboard[3]==' ' and drawboard[6] == secondmark):
                drawboard[3] = secondmark
                
            elif(drawboard[3] == drawboard[9] and drawboard[6]==' ' and drawboard[3] == secondmark):
                drawboard[6] = secondmark            
               
            elif(drawboard[1] == drawboard[5] and drawboard[9]==' ' and drawboard[1] == secondmark):
                drawboard[9] = secondmark
                
            elif(drawboard[5] == drawboard[9] and drawboard[1]==' ' and drawboard[5] == secondmark):
                drawboard[1] = secondmark
                
            elif(drawboard[1] == drawboard[9] and drawboard[5]==' ' and drawboard[1] == secondmark):
                drawboard[5] = secondmark
                
            elif(drawboard[3] == drawboard[5] and drawboard[7]==' ' and drawboard[3] == secondmark):
                drawboard[7] = secondmark
                
            elif(drawboard[5] == drawboard[7] and drawboard[3]==' ' and drawboard[5] == secondmark):
                drawboard[3] = secondmark
                
            elif(drawboard[3] == drawboard[7] and drawboard[5]==' ' and drawboard[3] == secondmark):
                drawboard[5] = secondmark
                
            elif(drawboard[1] == drawboard[2] and drawboard[3]==' ' and drawboard[1] == firstmark):
                drawboard[3]=secondmark
                
            elif(drawboard[1] == drawboard[3] and drawboard[2]==' ' and drawboard[1] == firstmark):
                 drawboard[5]=secondmark
                 
            elif(drawboard[2] == drawboard[3] and drawboard[1]==' ' and drawboard[3] == firstmark):
                 drawboard[1]=secondmark
                 
            elif(drawboard[4] == drawboard[5] and drawboard[6]==' ' and drawboard[4] == firstmark):
                 drawboard[6]=secondmark
                 
            elif(drawboard[4] == drawboard[6] and drawboard[5]==' ' and drawboard[4] == firstmark):
                 drawboard[5]=secondmark
                 
            elif(drawboard[5] == drawboard[6] and drawboard[4]==' ' and drawboard[5] == firstmark):
                 drawboard[4]=secondmark
                 
            elif(drawboard[7] == drawboard[8] and drawboard[9]==' ' and drawboard[7] == firstmark):
                 drawboard[9]=secondmark
                 
            elif(drawboard[7] == drawboard[9] and drawboard[8]==' ' and drawboard[7] == firstmark):
                 drawboard[8]=secondmark
                 
            elif(drawboard[8] == drawboard[7] and drawboard[7]==' ' and drawboard[8] == firstmark):
                 drawboard[7]=secondmark
                 
            elif(drawboard[1] == drawboard[4] and drawboard[7]==' ' and drawboard[1] == firstmark):
                 drawboard[7]=secondmark
                 
            elif(drawboard[1] == drawboard[7] and drawboard[4]==' ' and drawboard[1] == firstmark):
                 drawboard[4]=secondmark
                 
            elif(drawboard[4] == drawboard[7] and drawboard[1]==' ' and drawboard[4] == firstmark):
                 drawboard[1]=secondmark
                 
            elif(drawboard[2] == drawboard[5] and drawboard[8]==' ' and drawboard[2] == firstmark):
                 drawboard[8]=secondmark
                 
            elif(drawboard[2] == drawboard[8] and drawboard[5]==' ' and drawboard[2] == firstmark):
                 drawboard[5]=secondmark
                 
            elif(drawboard[5] == drawboard[8] and drawboard[2]==' ' and drawboard[5] == firstmark):
                 drawboard[2]=secondmark
                 
            elif(drawboard[3] == drawboard[6] and drawboard[9]==' ' and drawboard[3] == firstmark):
                 drawboard[9]=secondmark
                 
            elif(drawboard[3] == drawboard[9] and drawboard[6]==' ' and drawboard[3] == firstmark):
                 drawboard[6]=secondmark
            elif(drawboard[6] == drawboard[9] and drawboard[3]==' ' and drawboard[6] == firstmark):
                 drawboard[3]=secondmark
                 
            elif(drawboard[1] == drawboard[5] and drawboard[9]==' ' and drawboard[1] == firstmark):
                 drawboard[9]=secondmark
                 
            elif(drawboard[1] == drawboard[9] and drawboard[5]==' ' and drawboard[1] == firstmark):
                 drawboard[5]=secondmark
                 
            elif(drawboard[5] == drawboard[9] and drawboard[1]==' ' and drawboard[5] == firstmark):
                 drawboard[1]=secondmark
    
            elif(drawboard[3] == drawboard[5] and drawboard[7]==' ' and drawboard[3] == firstmark):
                 drawboard[7]=secondmark
                 
            elif(drawboard[3] == drawboard[7] and drawboard[5]==' ' and drawboard[3] == firstmark):
                 drawboard[5]=secondmark
                
            elif(drawboard[5] == drawboard[7] and drawboard[3]==' ' and drawboard[5] == firstmark):
                 drawboard[3]=secondmark
               
            else:   
                self.easy()
    
    
    
    def Game_Win_CompVPlayer(self):
           
        #Horizontal winning condition
        
        if(drawboard[1] == drawboard[2] and drawboard[2] == drawboard[3] and drawboard[1] == firstmark):    
              Game = 'Winplayer'
              
        elif(drawboard[4] == drawboard[5] and drawboard[5] == drawboard[6] and drawboard[4] == firstmark):    
              Game = 'Winplayer'
              
        elif(drawboard[7] == drawboard[8] and drawboard[8] == drawboard[9] and drawboard[7] == firstmark):    
              Game = 'Winplayer'
              
        #Vertical Winning Condition    
        elif(drawboard[1] == drawboard[4] and drawboard[4] == drawboard[7] and drawboard[1] == firstmark):    
              Game = 'Winplayer'    
        elif(drawboard[2] == drawboard[5] and drawboard[5] == drawboard[8] and drawboard[2] == firstmark):    
              Game = 'Winplayer'    
        elif(drawboard[3] == drawboard[6] and drawboard[6] == drawboard[9] and drawboard[3] == firstmark):    
              Game = 'Winplayer'   
        #Diagonal Winning Condition    
        elif(drawboard[1] == drawboard[5] and drawboard[5] == drawboard[9] and drawboard[5] == firstmark):    
              Game = 'Winplayer'    
        elif(drawboard[3] == drawboard[5] and drawboard[5] == drawboard[7] and drawboard[5] == firstmark):   
            Game = 'Winplayer'
    
        #Horizontal winning condition    
        elif(drawboard[1] == drawboard[2] and drawboard[2] == drawboard[3] and drawboard[1] == secondmark):    
             Game = 'Wincomp'    
        elif(drawboard[4] == drawboard[5] and drawboard[5] == drawboard[6] and drawboard[4] == secondmark):    
             Game = 'Wincomp'    
        elif(drawboard[7] == drawboard[8] and drawboard[8] == drawboard[9] and drawboard[7] == secondmark):    
             Game = 'Wincomp'    
        #Vertical Winning Condition    
        elif(drawboard[1] == drawboard[4] and drawboard[4] == drawboard[7] and drawboard[1] == secondmark):    
             Game = 'Wincomp'    
        elif(drawboard[2] == drawboard[5] and drawboard[5] == drawboard[8] and drawboard[2] == secondmark):    
             Game = 'Wincomp'    
        elif(drawboard[3] == drawboard[6] and drawboard[6] == drawboard[9] and drawboard[3] == secondmark):    
             Game = 'Wincomp'    
        #Diagonal Winning Condition    
        elif(drawboard[1] == drawboard[5] and drawboard[5] == drawboard[9] and drawboard[5] == secondmark):    
             Game = 'Wincomp'    
        elif(drawboard[3] == drawboard[5] and drawboard[5] == drawboard[7] and drawboard[5] == secondmark):    
            Game = 'Wincomp'
            
        #Match Tie or Draw Condition    
        elif(drawboard[1]!=' ' and drawboard[2]!=' ' and drawboard[3]!=' ' and drawboard[4]!=' ' and drawboard[5]!=' ' and drawboard[6]!=' ' and drawboard[7]!=' ' and drawboard[8]!=' ' and drawboard[9]!=' '):    
            Game = 'Draw'    
        else:            
            Game = 'Running'
          
        return(Game)
    
    
    def ext(self,cho,player,Symbol):
        if type_=='singleplayer':        
            drawboard[cho] = firstmark   
            player+=1    
            status=self.Game_Win_CompVPlayer()
            return player,status
        else:
             drawboard[cho] = Symbol    
             player+=1    
             status=self.Game_Win_vs1()
             return player,status
    
    def mainGame_code_CVP(self):
        global playerCVP
        
        Game = 'Running'
        playerCVP=random.randint(1,2)
       
        print("-"*200,'\n',sep='')
        print("\nThe empty board : \n")
        while(Game == 'Running'):
           
            self.Disp_Board()
            print("\n\n","-"*200,'\n',sep='')               
            
            if(playerCVP % 2 != 0):
                print("\nIt is your turn...")
                cho = int(input("Enter the position between [1-9] where you want to mark : "))
                print()
                while True:
                    if 1<=cho<=9:
                        if(self.Position_Check(cho)):    
                            playerCVP,Game=self.ext(cho,playerCVP,'')
                            break
                        else:
                            while True:
                                cho = int(input("\nAlready entered. Enter different position : "))
                                print()
                                if self.Position_Check(cho):                           
                                    playerCVP,Game=self.ext(cho,playerCVP,'')
                                    break
                            break
                       
                    else:
                        while True:
                            cho = int(input("\nPlease enter a position beteen 1 and 9 : "))
                            print()
                            if 1<=cho<=9:
                              if(self.Position_Check(cho)):    
                                playerCVP,Game=self.ext(cho,playerCVP,'')
                                break
                            else:
                                while True:
                                    cho = int(input("\nAlready entered. Enter different position : "))
                                    print()
                                    if self.Position_Check(cho):                           
                                        playerCVP,Game=self.ext(cho,playerCVP,'')
                                        break
                        break
                                    
            else:
                print("\nThe computer is playing...\n")
                time.sleep(2)
                if diff=='easy':
                    self.easy()
                    Game=self.Game_Win_CompVPlayer()
                    playerCVP+=1
                else:
                    self.hard()
                    Game=self.Game_Win_CompVPlayer()
                    playerCVP+=1
                    
    
        self.Disp_Board()    
        if(Game=='Draw'):    
            prtst="\nGame Draw..."
            for i in prtst:
                    print(i,end='')
                    time.sleep(.035)
        elif(Game=='Winplayer'):   
                prtst="\nCongrats! You defeated the computer and won the game!!"
                for i in prtst:
                    print(i,end='')
                    time.sleep(.035)
        elif(Game=='Wincomp'):    
                prtst="\nAlas! The computer defeated you!!"
                for i in prtst:
                    print(i,end='')
                    time.sleep(.035)
    
    
    def tyTXT(self):
            st= "\n\n\nThank you for playing Tic-Tac-Toe...\nGame Designed By : Nikhil Thomas Sojan 11-B\n\n"
            for i in st:
                print(i,end='')
                time.sleep(.07)
            print()
            print("\n","-"*200,'\n',sep='')
    
    
    def again(self):
            st = "\nDo you wish to play again : "
            for i in st:
                print(i,end='')
                time.sleep(.07)
            print()
            while True:
                cho = input().strip().lower()
                if cho == 'y':
                   print("\n\n","-"*200,'\n',sep='')
                   self.letsplay()           
                   break
                elif cho == 'n':
                   #go back to main menu code
                    break
                else:
                    cho = input("Enter y or n : ").strip().lower()
    
while True:
    print("Welcoeme to the Arcade")
    print('''We offer 3 games:
1. Tic Tac Toe
2. MasterMind
3. Othello''')
    while True:
        try:
            a = input("Enter Game: ")
            if a == '1' or a.lower() == 'tictactoe' or a.lower() == 'tic tac toe':
                a = 1
            elif a == '2' or a.lower == 'mastermind' or a.lower() == 'master mind':
                a = 2
            elif a == '3' or a.lower() == 'othello':
                a = 3
            else:
                raise Exception
            

        except:
            print("Invalid Option!")
            continue

        if a == 1:
            b = TicTacToe()
        elif a == 2:
            b = MasterMind()
        elif a == 3:
            b = Othello()

        ynl = ['y','ye','yes','yep','yup','yeah','yas','yass','yasss','yee',
       'n','no','nope','na','nah']
        while True:
            print("Do you want to play again? (y/n): ")
            f = input().lower().strip()
            if f in ynl:
                break
            else:
                print("\nERROR\n\n")      
        if f in ynl[:10]:
            continue
        else:
            print("Thank you for playing!")
            break
