import MasterMind
import Othello
import TicTacToe
import time

MasterMind.slowprint("Welcome to the Arcade!\n")
print('-'*50)
      
while True:
        print('''We offer 3 games:
1. Tic-Tac-Toe
2. MasterMind
3. Othello
''')
        while True:
                try:
                    a = input("Enter the game you want to play: ").lower().strip()
                    if a in ['1','tictactoe','tic tac toe','tic-tac-toe']:
                        a = 1
                    elif a in ['2','mastermind','master mind']:
                        a = 2
                    elif a in ['3','othello']:
                        a = 3
                    else:
                        raise Exception
                    break

                except:
                    print('-'*50)
                    MasterMind.slowprint("ERROR")
                    print("\n\nInvalid Option! Enter (1, 2 or 3)")
                    print('-'*50)
                    time.sleep(1)
                    continue

        MasterMind.newscreen(n=100)
        print('-'*100)
        if a == 1:
            TicTacToe.PlayGame()
        elif a == 2:
            MasterMind.PlayGame()
        elif a == 3:
            Othello.PlayGame()

        ynl = ['y','ye','yes','yep','yup','yeah','yas','yass','yasss','yee',
               'n','no','nope','na','nah']
        while True:
            MasterMind.slowprint("Do you want to play another game? (y/n): ")
            f = input().lower().strip()
            if f in ynl:
                break
            else:
                MasterMind.slowprint("\nERROR\n\n")      
        if f in ynl[:10]:
            MasterMind.newscreen()
            continue
        else:
            MasterMind.newscreen()
            print("Thank you for playing in the Arcade!")
            time.sleep(5)
            break
