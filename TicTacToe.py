#THIS IS STILL IN THE WORKS, THERE IS AN ISSUE WITH THE COMPUTER NOT ALWAYS CHOOSING THE WINNING MOVE
#GOALS:
#   1.ADD REPLAYABLILITY IN
# 

import random

class Player:
  def __init__(self,name,value):
    self.name = name
    self.value = value

def startBoard(board):
  print("   |   |   ")
  print(" "+board[6]+" | "+board[7]+" | "+board[8]+"  ")
  print("   |   |   ")
  print("-----------")
  print("   |   |   ")
  print(" "+board[3]+" | "+board[4]+" | "+board[5]+"  ")
  print("   |   |   ")
  print("-----------")
  print("   |   |   ")
  print(" "+board[0]+" | "+board[1]+" | "+board[2]+"  ")
  print("   |   |   ")

def theWelcome():
  print("This is TIC TAC TOE!\n")
  print("Instructions:\n1.The first to go will be random.\n2.To pick where to go, use the numberpad. The numbers correspond to the spot, below is an example.\n3.Enjoy!\n")
  startBoard(startingboard)

def whoStarts(x,y):
  return random.choice([x,y])

def theWinner(board,a):
  return(board[0] == a and board[3] == a and board[6] == a) or \
  (board[1] == a and board[4] == a and board[7] == a) or \
  (board[2] == a and board[5] == a and board[8] == a) or \
  (board[0] == a and board[1] == a and board[2] == a) or \
  (board[3] == a and board[4] == a and board[5] == a) or \
  (board[7] == a and board[8] == a and board[6] == a) or \
  (board[0] == a and board[4] == a and board[8] == a) or \
  (board[2] == a and board[4] == a and board[6] == a)

def copyBoard(board):
  copyboard = []
  for i in board:
    copyboard.append(i)
  return copyboard

def computerChoice(board):
  for i in range(9):
    copy = copyBoard(board)
    if copy[i] == " ":
      copy[i] = "O"
      if theWinner(copy,"O"):
        return True
      copy[i] = "X"
      if theWinner(copy,"X"):
        copy[i] = "O"
        return copy
  while True:
    choice = random.choice([0,1,2,3,4,5,6,7,8])
    if board[choice] == " ":
      board[choice] = "O"
      return board

    

commandWordsToStart = ["Y","YES"]
startingboard = ["1","2","3","4","5","6","7","8","9"]
playingboard = [" "] * 9
p1 = Player("Human",'X')
p2 = Player("Computer",'O')
theWelcome()
startGameInput = input("\n\nReady to start? Yes or No\n").upper()
while startGameInput not in commandWordsToStart:
  startGameInput = input("\n\nReady to start? Yes or No\n").upper()
else:
  starter = whoStarts(p1.value,p2.value)
  if starter == 'X':
    print(p1.name+" starts!")
  else:
    print(p2.name+" starts!")
  startBoard(playingboard)
  while True:
    if " " not in playingboard: #breaks out of loop if there is a draw
      break

    ####this is the players movement###
    if starter == 'X': 
      while True:
        try: #this will catch if the user enters in a non-numeric value
          location = int(input("Where will your move be?"))-1
        except ValueError:
          print("\nPlease enter in a value 1-9\n")
          continue #keeps looping until given the correct value
        else:
          break #if numeric, break
      
      if playingboard[location] == " ":
        playingboard[location] = 'X'
      else:
        print("Invalid move, try again!")
        continue #this will restart the while loop and reask where the user wants to go
      
      if theWinner(playingboard,p1.value):
        print(p1.name + " is the winner!")
        break
      print("\n\n")
      startBoard(playingboard)
      starter = 'O' #changes the turn back to the computer
    
    ####this is the computers movement####
    else: 
      decision = computerChoice(playingboard)
      if decision == True:
        print("Computer is the winner!")
        break
      else:
        playingboard = decision
        print("The computer picked")
        startBoard(playingboard)
        print("\n\n")
      starter = 'X' #changes the turn back to the player
  print("End Game")