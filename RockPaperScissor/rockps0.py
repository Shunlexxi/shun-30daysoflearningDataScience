#version 0
import random

print('Welcome! This is Rock Paper Scissor Game')

#rps declaration
def rps():
    keep_playing = True

    while keep_playing is True:
        player_input = input("Please, enter r, p or s for Rock, Paper or Scissor: ")
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
            print('Paper covers Rock, Computer wins!')
        
        elif player_input.lower() == 'p':
            if computer_input == 'r':
                print('Paper covers Rock, you win!')
            print('Scissor cuts paper, Computer wins!')
        
        elif player_input.lower() == 's':
            if computer_input == 'p':
                print('Scissor cuts Paper, you win!')
            print('Rock smashes Scissor, Computer wins!')


        choice = input("Would you like to keep playing? [y/n]: ")

        if choice.lower() == 'y':
            keep_playing = True
        
        elif choice.lower() == 'n':
            keep_playing = False

        print('Bye for now, hope to see you soon!')
rps()