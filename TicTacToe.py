import os    
import time
import random
import sys

def isIDLE():
   if "idlelib" in sys.modules:
      return True
   else:
      return False

def newscreen(n=75,t=0.6):
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

def slowprint(s,t=0.025):
   for i in s:
      print(i,end='')
      if isIDLE():
         time.sleep(t)

def PlayGame():
    global drawboard,type_,Game
    
    slowprint("Welcome to Tic-Tac-Toe!\n")
    print('-'*25)
    
    ynl = ['y','ye','yes','yep','yup','yeah','yas','yass','yasss','yee',
       'n','no','nope','na','nah']
    while True:
        Game = 'Running'
        drawboard = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        type_= ''
        
        choose ='''Choose your type of game:
1 - Single Player (Against Computer)
2 - Multi Player (Against another player)

Enter your choice: '''

        while True:
              if type_=='':
                 slowprint(choose)
              else:
                 slowprint(choose,0.004)
              type_ = input().strip().lower()
              try:
                 type_ = int(type_)
              except:
                 if type_ in ['single','single player','singleplayer']:
                     type_ = 1
                 elif type_ in ['multi','multi player','multiplayer']:
                     type_ = 2
                 else:
                     type_ = -1
              if type_ not in [1,2]:
                 print('-'*45)
                 slowprint("ERROR")
                 print("\n\nInvalid Choice! (Enter 1 or 2)")
                 print('-'*45)
                 time.sleep(1)
              else:
                 break

        if type_ == 1:
            newscreen()
            vsComputer()        
        else:
            newscreen()
            vs1()
            
        while True:
               slowprint("Do you want to play Tic-Tac-Toe again? (y/n): ")
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
           print("Thank you for playing Tic-Tac-Toe!\nGame created by: Nikhil Thomas Sojan")
           print('-'*40)
           newscreen(n=40,t=1.5)
           break  

def vs1():   
    rulesTXT()
    if isIDLE():
        newscreen()
    else:
        newscreen(t=2)
    print("\nPlayer 1 [X] --- Player 2 [O]\n")
    print('-'*75) 
    print('Let the games begin!!!')
    newscreen(t=1)
    
    mainGame_code_vs1()    
    
def vsComputer():
    global firstmark
    global secondmark
    rulesTXT()
    difficulty_choice()
    while True:

        firstmark = input("What do you want to play as? (X or O) : ").upper().strip()
        
        if firstmark not in ['O','X']:
             print('-'*45)
             slowprint("ERROR")
             print("\n\nInvalid Symbol! (Enter X or O)")
             print('-'*45)
             time.sleep(1)
             continue
        else:
            if firstmark == 'O':
                secondmark = 'X'
            else:
                secondmark = 'O'
            break
    

    newscreen()   
    print("\nPlayer [",firstmark,"] --- Computer [",secondmark,"]\n")
    print('-'*75) 
    print('Let the games begin!!!')
    newscreen(t=1)
    
    mainGame_code_CVP()
    
def rulesTXT():
    if type_ == 2:
        slowprint('''RULES FOR TIC-TAC-TOE (Multi-player):
1. The game is played on a grid that's 3 squares by 3 squares.
2. You are X, your friend is O. Players take turns putting their marks in empty squares.
3. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.
''')
    else:
        slowprint('''RULES FOR TIC-TAC-TOE (Single-player):
1. The game is played on a grid that's 3 squares by 3 squares.
2. Assume that you are X and the computer is O. Players take turns putting their marks in empty squares.
3. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.
''')
               
    print('-'*110)

def difficulty_choice():
    global diff
    op = ''
    choose = '''Choose your difficulty level:
1 - Easy
2 - Hard

Enter your choice: '''
    while True:
      if op=='':
         slowprint(choose)
      else:
         slowprint(choose,0.004)
      op = input().lower().strip()
      try:
         op = int(op)
      except:
         if op=='easy':
             op = 1
         elif op == 'hard':
             op = 2
         else:
             op = -1
      if op not in [1,2]:
         print('-'*45)
         slowprint("ERROR")
         print("\n\nInvalid Choice! (Enter 1 or 2)")
         print('-'*45)
         time.sleep(1)
      else:
         break
    if op==1:
        diff = 'easy'
    else:
        diff = 'hard'

    newscreen()

def mainGame_code_vs1():
    global player    
    player = 1
    Game = 'Running'
    
    Disp_Board()
    
    while(Game == 'Running'):
        
        if(player % 2 != 0):    
            print("Player 1's (X) turn:\n")    
            Symbol = 'X'    
        else:    
            print("Player 2's (O) turn:\n")    
            Symbol = 'O'
        while True:
            cho = input("Enter the position between [1-9] where you want to mark: ")
            try:
                cho = int(cho)
            except:
                print('-'*75)
                slowprint("ERROR")
                print("\n\nInvalid Attempt! Please enter digits only!")
                print('-'*75)
                time.sleep(1)
                continue
            if cho in range(1,10):
                if Position_Check(cho):
                    player,Game=ext(cho,player,Symbol)
                    break
                else:
                    print('-'*75)
                    slowprint("ERROR")
                    print("\n\nInvalid Attempt! This position is already occupied!")
                    print('-'*75)
                    time.sleep(1)
                    continue
            else:
                print('-'*75)
                slowprint("ERROR")
                print("\n\nInvalid Attempt! Please enter a valid position (1 - 9)")
                print('-'*75)
                time.sleep(1)
                continue

        newscreen()    
        Disp_Board()
    
    if(Game=='Draw'):
        print('-'*75)
        slowprint("Game Draw!\n")
        newscreen(t=1.5)
    elif(Game=='Win'):    
        player-=1    
        if(player%2!=0):
            print('-'*75)
            slowprint("Congratulations Player 1! You defeated player 2 and won the game!\n")
            newscreen(t=1.5)
        else:
            print('-'*75)
            slowprint("Congratulations Player 2! You defeated player 1 and won the game!\n")
            newscreen(t=1.5)

def Disp_Board():
    print()
    print(" %c │ %c │ %c " % (drawboard[1],drawboard[2],drawboard[3]),end='')
    print("\t\t\t 1 │ 2 │ 3 ")
    print("───┼───┼───",end='')
    print("\t\t\t───┼───┼───")
    print(" %c │ %c │ %c " % (drawboard[4],drawboard[5],drawboard[6]),end='')
    print("\t\t\t 4 │ 5 │ 6 ")
    print("───┼───┼───",end='')
    print("\t\t\t───┼───┼───")
    print(" %c │ %c │ %c " % (drawboard[7],drawboard[8],drawboard[9]),end='')
    print("\t\t\t 7 │ 8 │ 9 ")
    print()
    
def Position_Check(x):    
    if(drawboard[x] == ' '):    
        return True    
    else:    
        return False

def Game_Win_vs1():
        
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


def Emp_Pos(x):
    l=[]
    for i in range(1,len(drawboard)):
        if(drawboard[i] == ' '):    
             l.append(i)
    return l


def easy():       
        selection = Emp_Pos(drawboard)
        current_loc = random.choice(selection)
        drawboard[current_loc] = secondmark

def hard():
        
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
            
        elif(drawboard[1] == drawboard[3] and drawboard[2]==' ' and drawboard[1] == firstmark):  #ERROR Fixed
             drawboard[2]=secondmark
             
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
            easy()

def Game_Win_CompVPlayer():
       
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


def ext(cho,player,Symbol):
    if type_== 1:        
        drawboard[cho] = firstmark   
        player+=1    
        status=Game_Win_CompVPlayer()
        return player,status
    else:
         drawboard[cho] = Symbol    
         player+=1    
         status=Game_Win_vs1()
         return player,status

def mainGame_code_CVP():
    global playerCVP
    
    Game = 'Running'
    playerCVP=random.randint(1,2)
    
    Disp_Board()
    
    while(Game == 'Running'):
        if(playerCVP % 2 != 0):
            print("It is your turn:\n")
            while True:
                cho = input("Enter the position between [1-9] where you want to mark: ")
                try:
                    cho = int(cho)
                except:
                    print('-'*75)
                    slowprint("ERROR")
                    print("\n\nInvalid Attempt! Please enter digits only!")
                    print('-'*75)
                    time.sleep(1)
                    continue
                if cho in range(1,10):
                    if Position_Check(cho):
                        playerCVP,Game=ext(cho,playerCVP,'')
                        break
                    else:
                        print('-'*75)
                        slowprint("ERROR")
                        print("\n\nInvalid Attempt! This position is already occupied!")
                        print('-'*75)
                        time.sleep(1)
                        continue
                else:
                    print('-'*75)
                    slowprint("ERROR")
                    print("\n\nInvalid Attempt! Please enter a valid position (1 - 9)")
                    print('-'*75)
                    time.sleep(1)
                    continue
                                
        else:
            print("The computer is playing",end='')
            for i in range(3):
                sys.stdout.write('.')
                sys.stdout.flush()
                time.sleep(0.4)
            print()
            if diff=='easy':
                easy()
                Game=Game_Win_CompVPlayer()
                playerCVP+=1
            else:
                hard()
                Game=Game_Win_CompVPlayer()
                playerCVP+=1

        newscreen(t=0.4)
        Disp_Board()
    
    if(Game=='Draw'):
        print('-'*75)
        slowprint("Game Draw!\n")
        newscreen(t=1.5)
        
    elif(Game=='Winplayer'):
        print('-'*75)
        slowprint("Congratulations! You defeated the computer and won the game!\n")
        newscreen(t=1.5)
        
    elif(Game=='Wincomp'):
        print('-'*75)
        slowprint("Alas! The computer defeated you!\n")
        newscreen(t=1.5)
