# TicTacToe Project

# A brief welcome message with an illustration of the game:

Instructions = """
Welcome to TIC TAC TOE!

   |   |  
---|---|---
   |   |   
---|---|---
   |   |   

instructions:
1. The game is played on a grid of 3x3 squares.
2. Players will take turns putting their marks (O or X).
3. The first player to get 3 of their marks in a row is the winner.
4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.
"""

# For loop runs 9 times and fillts the 'spots' list with 9 ' ' (spaces).
# indicating that all positions are empty on the start. 

board = [' '] * 9


# Display_board() function is responsible for printing the CURRENT stat of the Tic Tac Toe board to the console.
# 'spots' list is used to display 'X' or 'O' in a 3x3 grid.


def display_board(board):
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---|---|---")


# The Player_input() function asks the player to input a number (1-9), which represents the position on the display board.
# It checks that the spot entered is valid, and if it is not blocked (by checking the index_list)


index_list = []

def player_input(player_name):
    while True:
        x = input(f'{player_name.title()}, Enter Row (1-9): ')
        
        if x.lower() == 'q' or x.lower() == 'quit':
            print("Exiting the game. Thanks for playing!")
            quit()

        if x.isdigit():
            x = int(x)
            x -= 1
            if 0 <= x < 9:
                if x in index_list:
                    print('This spot is blocked.')
                    continue
                index_list.append(x)
                return x
            else:
                print('Please enter a number between 1 and 9.')
        else:
            print("Only numbers between 1 and 9!")


# Check_win function checks if either player has won the game.
# The function iteratese over these winning combinations and checks if the marks 'X' or 'O' at those positions are the same and not ' '.
# If a player wins, the quit() function is initiated.


def check_win(board, player_one, player_two):
    winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]   
]

    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == 'X':
            print(f'{player_one.title()} has won the game!')
            quit('Thank you for playing!')
        elif board[combination[0]] == board[combination[1]] == board[combination[2]] == 'O':
            print(f'{player_two.title()} has won the game!')
            quit('Thank you for playing!')
        

# The play() function is the main function that starts the game.
# It enters a For loop, iterating 9 times, alternating turns between Player 1 and Player 2 using the modulo (i % 2) operator.
# After each player inputs their move, the board is updated, displayed, and checks for a winner.


def play():
  player_one = input("Enter player 1 name: ")
  player_two = input("Enter player 2 name: ")
  print(Instructions)
  print(f"{player_one.title()}'s sign is - X")
  print(f"{player_two.title()}'s sign is - O")
  display_board(board)
  for i in range(0,9):
    if i % 2 == 0:
      index = player_input(player_one)
      board[index] = 'X'
    else:
      index = player_input(player_two)
      board[index] = 'O'

    display_board(board)
    check_win(board, player_one, player_two)
  else:
    print("The game is a tie.")
    

# This line calls the play() function to start the game when the script is executed.
 
play()