# Nicholas Ivey 2/2/16 Week 4 

def printBoard(board):
    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################
     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
     print('-+-+-')
     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
     print('-+-+-')
     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')
    
    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board          #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################
    return ((board['top-L'] == player and board['top-M'] == player and board['top-R'] == player) or  # returns true if top row is complete
     (board['mid-L'] == player and board['mid-M'] == player and board['mid-R'] == player) or         # returns true if the middle row is complete
     (board['low-L'] == player and board['mid-M'] == player and board['mid-R'] == player) or         # returns true if the bottom row is complete
     (board['top-L'] == player and board['mid-L'] == player and board['low-L'] == player) or         # returns true if col 1 is complete
     (board['top-M'] == player and board['mid-M'] == player and board['low-M'] == player) or         # returns true if col 2 is complete
     (board['top-R'] == player and board['mid-R'] == player and board['low-R'] == player) or         # returns true if col 3 is complete
     (board['top-L'] == player and board['mid-M'] == player and board['low-R'] == player) or         # returns true if diagonal line is complete
     (board['top-R'] == player and board['mid-M'] == player and board['low-L'] == player))           # returns true if diagonal line is complete
    
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer   # Sets turn to startingPlaer string to define if X or O is playing 
    for i in range(9):      # loops through each sapce on the board
        printBoard(board)   # prints board to screen 
        print('Turn for ' + turn + '. Move on which space?')  
        move = input()      # takes user input for the desired move
        board[move] = turn  # sets the element at the inputed positon and sets it equal to X or O
        if( checkWinner(board, 'X') ): # checks if x is a winner
            print('X wins!')
            break
        elif ( checkWinner(board, 'O') ): # checks if o is a winner
            print('O wins!')
            break
    
        if turn == 'X': #  sets next turn to opposite player
            turn = 'O'
        else:
            turn = 'X'
        
    printBoard(board) # prints board following game
    