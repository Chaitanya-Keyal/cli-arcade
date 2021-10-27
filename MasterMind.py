import random as r
import os
import sys
from time import sleep

def cls():
   if os.name == 'posix':
      os.system('clear')
   else:
      os.system('cls')

def isIDLE():
   if "idlelib" in sys.modules:
      return True
   else:
      return False

def newscreen(t=3):
   if isIDLE():
      print('-'*100)
   else:
      sleep(t)
      cls()

def slowprint(s,t=0.035):
   for i in s:
      print(i,end='')
      if isIDLE():
         sleep(t)
slowprint('Welcome to MasterMind, The classic code-cracking game!',0.02)
print()
print('-'*100)

def rules():
    slowprint('''Rules to play:
1. The code-maker (Computer) will generate a 4 digit code (X X X X) based on the chosen level.
2. The code-breaker (You) has to break this code,
   by duplicating its exact digits and positions.
3. The attempts can be entered in any of the following formats:
\tX X X X
\tXXXX
4. After every attempt,
   clues will be given on the left side of the board, indicated by 2 pegs:
\ti.  White Peg (W) - For every correct digit that is placed in the wrong position.
\tii. Red Peg (R)   - For every correct digit that is placed in the correct position as well.
5. The order of these pegs does NOT matter.
6. A total of 10 attempts are allowed before the game is over, and the code is revealed.
7. The Aim of the game is to break the code within 10 attempts.''',0)
    print()
    print('-'*100)

code = []
codedisp = ['X','X','X','X']
plist = []
alist = []

for i in range(10):
    plist.append(['-','-','-','-'])
    alist.append(['-','-','-','-']) 
counter = 0

def coder():
    global code
    lvl = {1:6,2:7,3:8,4:9}
    choose = '''Choose your level:
1 - Easy
2 - Medium
3 - Difficult
4 - Insane

Enter your choice: '''
    op = ''
    while True:
      if op=='':
         slowprint(choose)
      else:
         slowprint(choose,0.005)
      op = int(input())
      if op not in [1,2,3,4]:
         slowprint("\nERROR")
         print("\n\nInvalid Choice! (Enter 1,2,3 or 4)")
         print('-'*35)
      else:
         break
    for i in range(4):
        code.append(r.choice([i for i in range(1,lvl[op])]))
    print('-'*100)
    slowprint("The code has been generated! Start Cracking!")
    print()
        
def board():
    global codedisp
    for i in plist:
        if i==['R','R','R','R'] or counter==9:
            codedisp = code
    print('┌───────┬─────┬─────┬─────┬─────┐')
    print('│ Code: │',end='')
    for i in codedisp:
        print(' ',i,' │',end='')
    print()
    print('├───────┼─────┼─────┼─────┼─────┤')
    for i in range(1,11):
          print('│',plist[-i][0],' ',plist[-i][1],'│     │     │     │     │')
          print('│',plist[-i][2],' ',plist[-i][3],'│',end='')
          for j in range(4):
              print(' ',alist[-i][j],' │',end='')
          print()
          if i==10:
              print('└───────┴─────┴─────┴─────┴─────┘')
          else:
              print('├───────┼─────┼─────┼─────┼─────┤')
    print('-'*100)
    
def breaker():
    global alist, plist
    pegs = ['-','-','-','-']
    while True:
        attempt = [int(i) for i in input("\nYour Attempt: ").split()]
        if not len(attempt)==4:
            print("\nInvalid Attempt! Please enter exactly 4 digits!")
        else:
            for i in attempt:
                if not type(i)==type(1):
                    print("\nInvalid Attempt! Please enter digits only!")
                    break
            alist[counter-1]=attempt
            break
    for i in range(4):
        if attempt[i] in code:
            if attempt[i]==code[i]:
                pegs[i] = 'R'
            else:
                pegs[i] = 'W'
    r.shuffle(pegs)
    for i in range(4):
        if pegs[i]=='-':
            pegs=list('-')+pegs[:i]+pegs[i+1:]
    print(pegs)
    plist[counter-1]=pegs

def play():
    global codedisp,counter
    coder()
    print(code)
    while True:
        if code in alist:
            newscreen()
            board()
            slowprint("Congratulations! You cracked the code!")
            sleep(5)
            break
        elif counter==10:
            newscreen()
            board()
            slowprint("Sorry, you have lost! The correct code is displayed on the board!")
            sleep(5)
            break
        counter+=1
        newscreen()
        board()
        slowprint("Attempt "+str(counter)+":")
        breaker()
rules()
play()
#do you want to play again?
#yes-
    #do you want the rules again?
    #yes-
        #rules() level()
    #no- level()
    #play()
#no - thank you for playing()
