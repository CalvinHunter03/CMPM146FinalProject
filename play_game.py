from Player import Player
from Game import Game

# Loop until player quits game
turn = True #when true, players turn
while(1):

    # Init for player
    player = Player()
    game = Game(player)

    # Loop until game ends
    while not game.over:
        game.start_round() # Start a round of the game

        # Play the game #

        round_over = False
        turn = 0
        while round_over == False:
            game.clear_console()
            # Player's turn
            # print("Your turn")

            ##########################
            # Input player turn here #
            ##########################

            # print(f"{game.enemy.name}'s turn")

            ############################
            # Generate enemy turn here #
            ############################
            
            turn += 1 
            game.display_game(player)
        game.check_end()

    # # just commenting this out for now as I don't know where to put it
    # if (turn):
    #     #give player options about moving
    #     #two attack options, dodge option
    #     #heal
    #     #move towards / away from enemy
    #     print(f'player makes move')
        
    # else: #enemy / bot turn
    #     print(f'bot makes move')


