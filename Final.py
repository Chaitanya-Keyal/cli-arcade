import random
import os
import sys
import copy
import time

class Othello:
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
    

    def isIDLE(self):
        globals().update(self.__dict__)
        if "idlelib" in sys.modules:
          return True
        else:
          return False
    
    def newscreen(self,n=105,t=0.6):
        globals().update(self.__dict__)
        print("\nLoading",end='')
        for i in range(3):
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(t)
        print()
        if self.isIDLE():
            print('-'*n)
        else:
            if os.name == 'posix':
                os.system('clear')
            else:
                os.system('cls')
    
    def Legend():
        pass
    
    def Print(self, copy):
        globals().update(self.__dict__)
        pieces = self.pieces
        marker = self.marker
        vedge = self.vedge
        board = self.board
        rplus = self.rplus
        lplus = self.lplus
        plus = self.plus
        line = 0
        def Line(line):
            space = 8
            if line == 0:
                s = ""
                s += " "+ self.ulcorner
                s += (self.hedge*3 + self.dplus)*7 + self.hedge*3 + self.urcorner
    
                s += ' '*space
                s += " "+ self.ulcorner
                s += (self.hedge*3 + self.dplus)*7 + self.hedge*3 + self.urcorner
                return s
                
            elif line == 16:
                s = ' '
                s += self.dlcorner + self.hedge*3 + (self.uplus + self.hedge*3)*7 + self.drcorner
    
                s += ' '*space + ' '
                s += self.dlcorner + self.hedge*3 + (self.uplus + self.hedge*3)*7 + self.drcorner
                return s
    
            elif line == 17:
                s = '   '
                for i in range(8):
                    s += chr(ord('A')+i) + ' '*3
    
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
                if line == 7 or line == 9:
                    s += ' '*(space//2 - 1) + '⟶'*1 + ' '*(space//2 )
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
                s += rplus + self.hedge*3 + (plus + self.hedge*3)*7 + lplus
                if line == 8:
                    s += ' '*(space//2 - 1) + '⟶'*1 + ' '*(space//2 )
                else:
                    s += ' '*space
                s += ' '
                s += rplus + self.hedge*3 + (plus + self.hedge*3)*7 + lplus
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
        move = self.move
        for i in range(8):
            for j in range(8):
                if move((i,j),player,True):
                    return True
        return False
    
    def Play(self):
        board = self.board
        marker = self.marker
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
        board = self.board
        pieces = self.pieces
        dcnt = self.dcnt

        player = -1
        Player = 1
        self.Print(board)
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
                lcopy = self.copy.deepcopy(board)
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
        board = self.board
        pieces = self.pieces
        dcnt = self.dcnt
        player = -1
        Player = 'Player'
        self.Print(board)
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
                    lcopy = self.copy.deepcopy(board)
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
                lcopy = self.copy.deepcopy(board)
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
        board = self.board
        pieces = self.pieces
        dcnt = self.dcnt
        while True:
            try:
                sleep = int(input("Enter time(in ms) to wait between each move: ")) / 1000
                break
            except:
                print("Invalid time")
    
        player = -1
        Player = 1
        self.Print(board)
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
        board = self.board
        pieces = self.pieces
        dcnt = self.dcnt
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

    @staticmethod
    def Oth(self):
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
                self.newscreen()
                continue
            else:
                self.newscreen()
                print("Thank you for playing Othello!")
                time.sleep(5)
                break
    def __init__(self):
        self.Oth(self)

class MasterMind:

    def isIDLE(self):
       if "idlelib" in sys.modules:
          return True
       else:
          return False
    
    def newscreen(self,n=105,t=0.6):
        print("\nLoading",end='')
        for i in range(3):
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(t)
        print()
        if self.isIDLE():
            print('-'*n)
        else:
            if os.name == 'posix':
                os.system('clear')
            else:
                os.system('cls')
    
    def slowprint(self,s,t=0.035):
       for i in s:
          print(i,end='')
          if self.isIDLE():
             time.sleep(t)
    
    def createDict(l):
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
    
    valid = []
    lvl = {1:7,2:8,3:9,4:10}
    levelname = {1:"Easy",2:"Medium",3:"Difficult",4:"Insane"}
    code,codedisp,plist,alist,op,counter=[],[],[],[],'',0
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
            self.slowprint(choose)
          else:
            self.slowprint(choose,0.004)
          op = input()
          try:
             op = int(op)
          except:
             op = self.getKey(op.title())
          if op not in self.levelname:
             print('-'*45)
             self.slowprint("ERROR")
             print("\n\nInvalid Choice! (Enter 1, 2, 3 or 4)")
             print('-'*45)
             time.sleep(1)
          else:
             break
        valid = [i for i in range(1,self.lvl[op])]
        for i in range(4):
            code.append(random.choice(valid))
        print('-'*45)
        self.slowprint("The code has been generated! Start Cracking!\n")
    
    def board_rules():
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
    
    def board():
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
            self.slowprint("\nYour Attempt: ",0.02)
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
               self.slowprint("ERROR")
               print("\n\nInvalid Attempt! Please enter digits only!")
               print('-'*105)
               time.sleep(1)
               continue
            if len(temp) != 4:
               print('-'*105)
               self.slowprint("ERROR")
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
               self.slowprint("ERROR")
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
                self.newscreen()
                codedisp = code
                self.board()
                if code in alist:
                   self.slowprint("Congratulations!\nYou cracked the code in only "+str(counter)+" attempts!\n")
                else:
                   self.slowprint("Sorry, you have lost!\nThe correct code is displayed on the board!\n")
                self.newscreen(t=2.5)
                break
            counter+=1
            self.newscreen()
            self.board_rules()
            self.leveldisplay()
            self.slowprint("Attempt "+str(counter)+":\n")
            self.breaker()
    
    ynl = ['y','ye','yes','yep','yup','yeah','yas','yass','yasss','yee',
           'n','no','nope','na','nah']
    
    
    def MM(self):
        while True:
            self.initialize()
            self.play()
            while True:
                self.slowprint("Do you want to play MasterMind again? (y/n): ")
                f = input().lower().strip()
                if f in self.ynl:
                    break
                else:
                    self.slowprint("\nERROR\n\n")      
            if f in self.ynl[:10]:
                self.newscreen()
                continue
            else:
                self.newscreen()
                print("Thank you for playing MasterMind!")
                time.sleep(5)
                break

    def __init__(self):
        self.MM(self)

obj = MasterMind()
    

    
    