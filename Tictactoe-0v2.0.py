import os    
import time
import random

#Symbol = 'X'


def letsplay():
    global drawboard
    global type_
    global Game
    
    welcomeTXT()
    print('\t\t\t\t\t\t\t\t\t\t\t\t',"="*22,sep='')
    
    loadingTXT()

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
        vsComputer()        
    else:
         print("\n\n","-"*200,'\n',sep='')
         vs1()
         
    again()
                

def welcomeTXT():
    print("\t\t\t\t\t\t\t\t\t\t\t\t",end='')
    st= "Welcome to Tic-Tac-Toe"
    for i in st:
        print(i,end='')
        time.sleep(.10)
    print()


def vs1():   
    rulesTXT()
    loadingTXT()
    print("\n\n","-"*200,'\n',sep='')
    print('Let the games begin!!!\n')
    print("","-"*200,'\n',sep='')
    print("\nPlayer 1 [X] --- Player 2 [O]\n")
    time.sleep(1)
    print()
    mainGame_code_vs1()   
    tyTXT()
    
    

def vsComputer():
    global firstmark
    global secondmark
    rulesTXT()
    loadingTXT()
    difficulty_choice()
    loadingTXT()
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
    loadingTXT()
    print("","-"*200,'\n',sep='')  
    print('Let the games begin!!!\n\n')
    
    mainGame_code_CVP()
    
    tyTXT()  
    
        


#Displays the rules of the game
def rulesTXT():
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
def loadingTXT():    
    print("\nLoading, Please Wait ",end='')
    for i in range(5):
        print("." , end=" ")
        time.sleep(1)
    print()
    print()
    print()


def difficulty_choice():
    global diff
    diff = input("Do you wish to play at easy or hard difficulty : ").lower().strip()
    while True:        
        if diff not in ['easy','hard']:
            diff = input("Please enter 'easy' for easy difficulty and 'hard' for hard difficulty... : ").lower().strip()
        else:
            break
    print("\n\n","-"*200,'\n',sep='')


def mainGame_code_vs1():
    global player    
    player = 1
    Game = 'Running'
    print("-"*200,'\n',sep='')
    print("\nThe empty board : \n")
    while(Game == 'Running'):
        
        Disp_Board()
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
            if(Position_Check(cho)):    
               player,Game=ext(cho,player,Symbol)
            else:
                while True:
                    cho = int(input("\nAlready entered. Enter different position : "))
                    print()
                    if Position_Check(cho):                   
                        player,Game=ext(cho,playe,Symbolr)
                        break
        else:
            while True:
                    cho = int(input("\nPlease enter a position beteen 1 and 9 : "))
                    print()
                    if Position_Check(cho):
                         player,Game=ext(cho,player,Symbol)
                         break
    Disp_Board()    
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


def Disp_Board():    
    print(" %c | %c | %c " % (drawboard[1],drawboard[2],drawboard[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (drawboard[4],drawboard[5],drawboard[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (drawboard[7],drawboard[8],drawboard[9]))    
    print("   |   |   ")


def Position_Check(x):    
    if(drawboard[x] == ' '):    
        return True    
    else:    
        return False

def Game_Win_vs1():    
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
    if type_=='singleplayer':        
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
   
    print("-"*200,'\n',sep='')
    print("\nThe empty board : \n")
    while(Game == 'Running'):
       
        Disp_Board()
        print("\n\n","-"*200,'\n',sep='')               
        
        if(playerCVP % 2 != 0):
            print("\nIt is your turn...")
            cho = int(input("Enter the position between [1-9] where you want to mark : "))
            print()
            while True:
                if 1<=cho<=9:
                    if(Position_Check(cho)):    
                        playerCVP,Game=ext(cho,playerCVP,'')
                        break
                    else:
                        while True:
                            cho = int(input("\nAlready entered. Enter different position : "))
                            print()
                            if Position_Check(cho):                           
                                playerCVP,Game=ext(cho,playerCVP,'')
                                break
                        break
                   
                else:
                    while True:
                        cho = int(input("\nPlease enter a position beteen 1 and 9 : "))
                        print()
                        if 1<=cho<=9:
                          if(Position_Check(cho)):    
                            playerCVP,Game=ext(cho,playerCVP,'')
                            break
                        else:
                            while True:
                                cho = int(input("\nAlready entered. Enter different position : "))
                                print()
                                if Position_Check(cho):                           
                                    playerCVP,Game=ext(cho,playerCVP,'')
                                    break
                    break
                                
        else:
            print("\nThe computer is playing...\n")
            time.sleep(2)
            if diff=='easy':
                easy()
                Game=Game_Win_CompVPlayer()
                playerCVP+=1
            else:
                hard()
                Game=Game_Win_CompVPlayer()
                playerCVP+=1
                

    Disp_Board()    
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


def tyTXT():
        st= "\n\n\nThank you for playing Tic-Tac-Toe...\nGame Designed By : Nikhil Thomas Sojan 11-B\n\n"
        for i in st:
            print(i,end='')
            time.sleep(.07)
        print()
        print("\n","-"*200,'\n',sep='')


def again():
        st = "\nDo you wish to play again : "
        for i in st:
            print(i,end='')
            time.sleep(.07)
        print()
        while True:
            cho = input().strip().lower()
            if cho == 'y':
               print("\n\n","-"*200,'\n',sep='')
               letsplay()           
               break
            elif cho == 'n':
               #go back to main menu code
                break
            else:
                cho = input("Enter y or n : ").strip().lower()


letsplay()
