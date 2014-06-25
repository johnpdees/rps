##This program plays 3 games of rock, paper, scissors

## imports input program
from subber_choice import choice

def tie():
    print("It's a tie!")
def rock():
    print ("Rock Wins!!")
def paper():
    print ("Paper Wins!!")
def scis():
    print ("Scissors Wins!!")


## compare player 1 and 2 choices    
def compare(choice1, choice2):
    """compares rock, paper, and scissors"""
    if choice1 == 'rock':
        if choice2 == 'rock':
            tie()
            return 0
        elif choice2 == 'paper':
            paper()
            return 2
        elif choice2 == 'scissors':
            rock()
            return 1
    elif choice1 == 'paper':
        if choice2 == 'rock':
            paper()
            return 1
        elif choice2 == 'paper':
            tie()
            return 0
        elif choice2 == 'scissors':
           scis()
           return 2
    else:
        if choice2 == 'rock':
            rock()
            return 2
        elif choice2 == 'paper':
            scis()
            return 1
        elif choice2 == 'scissors':
           tie()
           return 0

counter = 0
p1 = 0
p2 = 0

player1_name = raw_input("Enter player 1 name: ")
player2_name = raw_input("Enter player 2 name: ")

## Calls Game 3 times
while counter != 3:
  choice1 = choice()
  choice2 = choice()
  test = compare(choice1, choice2)
  if test == 1:
      p1 += 1
  elif test == 2:
      p2 += 1
  counter += 1

if p1 > p2:
    message = 'Player 1 Wins!'
elif p2 > p1:
    message = 'Player 2 Wins!'
else:
    message = 'It is a TIE!'

print ('{} scored: {}    {} scored: {}'.format(player1_name,p1,player2_name, p2))
print message
print ("Thanks for playing!!")


