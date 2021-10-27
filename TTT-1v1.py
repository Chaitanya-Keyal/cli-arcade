import os    
import time    
    
drawboard = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
player = 1    
   
########win Flags##########    
Win = 1    
Draw = -1    
Running = 0    
Stop = 1    
###########################    
Game = Running    
Symbol = 'X'    
   
#This Function Draws Game Board    
def Disp_Board():    
    print(" %c | %c | %c " % (drawboard[1],drawboard[2],drawboard[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (drawboard[4],drawboard[5],drawboard[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (drawboard[7],drawboard[8],drawboard[9]))    
    print("   |   |   ")    
   
#This Function Checks position is empty or not    
def Position_Check(x):    
    if(drawboard[x] == ' '):    
        return True    
    else:    
        return False    
   
#This Function Checks player has won or not    
def Game_Win():    
    global Game    
    #Horizontal winning condition    
    if(drawboard[1] == drawboard[2] and drawboard[2] == drawboard[3] and drawboard[1] != ' '):    
        Game = Win    
    elif(drawboard[4] == drawboard[5] and drawboard[5] == drawboard[6] and drawboard[4] != ' '):    
        Game = Win    
    elif(drawboard[7] == drawboard[8] and drawboard[8] == drawboard[9] and drawboard[7] != ' '):    
        Game = Win    
    #Vertical Winning Condition    
    elif(drawboard[1] == drawboard[4] and drawboard[4] == drawboard[7] and drawboard[1] != ' '):    
        Game = Win    
    elif(drawboard[2] == drawboard[5] and drawboard[5] == drawboard[8] and drawboard[2] != ' '):    
        Game = Win    
    elif(drawboard[3] == drawboard[6] and drawboard[6] == drawboard[9] and drawboard[3] != ' '):    
        Game = Win    
    #Diagonal Winning Condition    
    elif(drawboard[1] == drawboard[5] and drawboard[5] == drawboard[9] and drawboard[5] != ' '):    
        Game = Win    
    elif(drawboard[3] == drawboard[5] and drawboard[5] == drawboard[7] and drawboard[5] != ' '):    
        Game=Win    
    #Match Tie or Draw Condition    
    elif(drawboard[1]!=' ' and drawboard[2]!=' ' and drawboard[3]!=' ' and drawboard[4]!=' ' and drawboard[5]!=' ' and drawboard[6]!=' ' and drawboard[7]!=' ' and drawboard[8]!=' ' and drawboard[9]!=' '):    
        Game=Draw    
    else:            
        Game=Running    

st= "Welcome to Tic-Tac-Toe"

for i in st:
    print(i,end='')
    time.sleep(.15)
print()
st='''
RULES FOR TIC-TAC-TOE

1. The game is played on a grid that's 3 squares by 3 squares.

2. You are X, your friend (or the computer in this case) is O. Players take turns putting their marks in empty squares.

3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.

4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.'''
for i in st:
    print(i,end='')
    time.sleep(.03)


print("Player 1 [X] --- Player 2 [O]\n")    
print()    
print()    
print("Please Wait...")    
time.sleep(3) #Loading Time
print('\n\nLet the games begin!!!\n\n')
#Game running code
while(Game == Running):   
    Disp_Board()
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
            drawboard[cho] = Symbol    
            player+=1    
            Game_Win()
        else:
            while True:
                cho = int(input("\nAlready entered. Enter different position : "))
                print()
                if Position_Check(cho):
                   
                    drawboard[cho] = Symbol    
                    player+=1    
                    Game_Win()
                    break
    else:
        while True:
                cho = int(input("\nPlease enter a position beteen 1 and 9 : "))
                print()
                if Position_Check(cho):
                     drawboard[cho] = Symbol    
                     player+=1    
                     Game_Win()
                     break
     
  
Disp_Board()    
if(Game==Draw):    
    print("Game Draw")    
elif(Game==Win):    
    player-=1    
    if(player%2!=0):    
        print("\nPlayer 1 Won!!")    
    else:    
        print("\nPlayer 2 Won!!") 
    
        
    
     
