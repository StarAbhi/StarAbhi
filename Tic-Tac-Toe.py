''' We will make the board using dictionary 
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choice of move. '''

theBoard = {'0': ' ' , '1': ' ' , '2': ' ' ,
            '3': ' ' , '4': ' ' , '5': ' ' ,
            '6': ' ' , '7': ' ' , '8': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''

def printBoard(board):
    print(board['0'] + '|' + board['1'] + '|' + board['2'])
    print('-+-+-')
    print(board['3'] + '|' + board['4'] + '|' + board['5'])
    print('-+-+-')
    print(board['6'] + '|' + board['7'] + '|' + board['8'])

# Now we'll write the main function which has all the gameplay functionality.
def game():
    print('''     Implementation of Two Player Tic-Tac-Toe game. 
    Choose the move by numeric number by below board.
    After game over if you want to restart game type 'Y' . ''')
    print('0' + '|' + '1' + '|' + '2')
    print('-+-+-')
    print('3' + '|' + '4' + '|' + '5')
    print('-+-+-')
    print('6' + '|' + '7' + '|' + '8')

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(theBoard)
        move = input(  turn + "'s turn . Input Move ( 0 - 8 ) : ");        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nChoose other place ?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if theBoard['6'] == theBoard['7'] == theBoard['8'] != ' ': # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif theBoard['3'] == theBoard['4'] == theBoard['5'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['0'] == theBoard['1'] == theBoard['2'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['0'] == theBoard['3'] == theBoard['6'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['6'] == theBoard['4'] == theBoard['2'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['0'] == theBoard['4'] == theBoard['8'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "

        game()

if __name__ == "__main__":
    game()