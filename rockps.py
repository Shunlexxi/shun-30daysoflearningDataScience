
import random

def aesthetics():

    print('----------------------------------------------------------------')


print('Welcome! This is Rock Paper Scissor Game')

aesthetics()

#rps declaration
def rps():

    lives = int(input('Please, enter the no of time(s) you would love to play [Numbers only]: '))
       
    aesthetics()

    while lives > 0:
        player_input = input("PLAYING: Enter r, p or s for Rock, Paper or Scissor: ")
        possible_actions = ['r', 'p', 's']
        computer_input = random.choice(possible_actions)

        print(f'You chose {player_input} and the computer chose {computer_input}')

        #Same input
        if player_input.lower() == computer_input:
            print(f"Both Players chose {player_input}, so it's a tie!")


        #different input
        elif player_input.lower() == 'r':
            if computer_input == 's':
                print('Rock smashes Scissor, you win!')
            else:
                print('Paper covers Rock, Computer wins!')
        
        elif player_input.lower() == 'p':
            if computer_input == 'r':
                print('Paper covers Rock, you win!')
            else:
                print('Scissor cuts paper, Computer wins!')
        
        elif player_input.lower() == 's':
            if computer_input == 'p':
                print('Scissor cuts Paper, you win!')
            else:
                print('Rock smashes Scissor, Computer wins!')
            
        aesthetics()
        #subtract live
        lives -= 1

rps()