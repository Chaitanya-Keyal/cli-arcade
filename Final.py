import MasterMind
import Othello
import TicTacToe

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
            TicTacToe.letsplay()
        elif a == 2:
            MasterMind.PlayGame()
        elif a == 3:
            Othello.Oth()

        ynl = ['y','ye','yes','yep','yup','yeah','yas','yass','yasss','yee',
       'n','no','nope','na','nah']
        while True:
            print("Do you want to play MasterMind again? (y/n): ")
            f = input().lower().strip()
            if f in ynl:
                break
            else:
                print("\nERROR\n\n")      
        if f in ynl[:10]:
            continue
        else:
            print("Thank you for playing MasterMind!")
            break