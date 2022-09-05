import os
import numpy as np

game_data = np.array([[0, 0, 0], 
                     [0, 0, 0],
                     [0, 0, 0]])

symbols = [' ', 'o', '*']

inputed = False

running = True

turn = 1



def gameboard():
    global drawn
    drawn = False
    while drawn == False:
        for x in range(3):

            print("-------------------------------------")
            for i in range(4):
                print("|           |           |           |")
                if i == 1:
                    print("|     " + symbols[game_data[x, 0]] + "     |     " + symbols[game_data[x, 1]] + "     |     " + symbols[game_data[x, 2]] + "     |")
        else:
            print("-------------------------------------")
            drawn = True

def clear():
    drawn = False
    os.system("clear")



def check_winner():
    win = np.array([[1, 1, 1], [2, 2, 2]])
    for x in range(2):
        for i in range(3):
            if np.array_equal(win[x], game_data[i]):
                print('winner is ' + str(x+1))
                return True
            elif np.array_equal(win[x], game_data[:, i]):
                print('winner is ' + str(x+1))
                return True
            elif i == 0:
                if (np.array_equal(win[x], [game_data[i][i], game_data[i+1][i+1], game_data[i+2][i+2]])) or (np.array_equal(win[x], [game_data[i][i+2], game_data[i+1][i+1], game_data[i+2][i]])):
                    print('winner is ' + str(x+1))
                    return True
            else:
                pass



def get_input():
    y = int(input('choose column:')) - 1
    x = int(input('choose row:')) - 1
    if x+1 in [1, 2, 3] and y+1 in [1, 2 ,3]:
        if game_data[x, y] != 0:
            print('sqaure has been taken, please reinput')
        else:
            global turn
            global inputed
            game_data[x, y] = turn
            turn = 3 - turn
            clear()
    else:
        print('sqaure does not exist, please reinput')

    
clear()
while running:
    if check_winner():
        if input("do you wish to play again? y/n:") == 'y':
            game_data = np.array([[0, 0, 0], [0, 0, 0],[0, 0, 0]])
            continue
        else:
            quit()
    elif 0 not in game_data:
        print('game was a tie')
        quit()
    else:
        gameboard()
        get_input()