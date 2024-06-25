import os
import random

# displaying the board

board = [' ']*10
def display_board(board):
   
  os.system('cls')
  print(board[7] + '|' + board[8] + '|' + board[9])
  print('-----')
  print(board[4] + '|' + board[5] + '|' + board[6])
  print('-----')
  print(board[1] + '|' + board[2] + '|' + board[3])
  print('-----')


#Asking player marker choice
def player_marker_choice():
  marker = ''
  while marker != 'X' and marker != 'O':
    marker = input('Player1: Do you want to take X or O ?').upper()
  if marker == 'X':
    return ('X','O')
  else:
    return ('O','X')

#deciding, who will play first
def play_first():
 selected_num = random.randint(1,2)
 if selected_num == 1:
   return 'Player1'
 else:
   return 'Player2'

#player position choice
def player_position_choice(board):
  position = 0
  while position not in range(1,10) or not check_space(board,position):
    position = int(input('Please enter a position between 1 and 9: '))
  return position


#Placing the marker
def place_marker(board,position,marker):
  board[position] = marker

#checkinng if a playerwith a marker has won a game

def check_win(board,mark):
  #checking all the horizontal rows
  if ((board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or (board[7] == board[8] == board[9] == mark)):
    return True
  
  #checking all the vertical columns
  if((board[1] == board[4] == board[7]== mark) or (board[2] == board[5] == board[8]== mark )or (board[3] == board[6] == board[9]== mark)):
    return True
  
  #checking diagonal columns
  if((board[1] == board[5] == board[9]== mark) or (board[3] == board[5] == board[7]== mark)):
    return True
  
#checking if there any space is left on the board
def check_space(board,position):
  if board[position] == ' ':
    return True
  else:
    return False

#checking if board is full
def full_board(board):
  for i in range(1,9):
    if check_space(board,i):
      return False
  return True

#asking player if they want to play again
def play_again():
  status = input('Want to play again ? Please enter Yes or No: ').lower()
  return status


#Driver function
while True:
  print('****Welcome to Tic Tac Toe****')
  #reseting the game
  board = [' ']*10
  Player1_marker,Player2_marker  = player_marker_choice()
  player_turn = play_first()
  print(f'{player_turn} will play first')
  
  #Asking a user if they are ready to play
  start_game = input('Are you ready to play ? Y or N: ')
  if start_game == 'Y':
    game_on = True
  else:
    game_on = False
  

  while game_on:
    if player_turn == 'Player1':
      display_board(board)
      position = player_position_choice(board)
      place_marker(board,position,Player1_marker)
       
      #checking if player 1 has won 
      if check_win(board,Player1_marker):
        display_board(board)
        print('Congratulations Player1, You have won the game')
        game_on = False
      #checking if board was full and is it a tie
      else:
        if full_board(board):
          display_board(board)
          print('It is a tie')
          game_on = False
          break
        else:
          player_turn = 'Player2'
    
    else:
      display_board(board)
      position = player_position_choice(board)
      place_marker(board,position,Player2_marker)

      if check_win(board,Player2_marker):
        display_board(board)
        print('Congratulations Player2, You have won the game')
        game_on = False
      else:
        if full_board(board):
          display_board(board)
          print('It is a tie')
          game_on = False
          break
        else:
          player_turn = 'Player1'
  if not play_again():
    break