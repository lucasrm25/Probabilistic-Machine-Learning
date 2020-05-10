    
def play_battleships(player1, player2):
    """
    Play battleships
    :param player1, player2: Select players from agents 'human', 'random', 'MC', 'MC2'
    """
    import game

    game = game.Game(size = 10, ships = [5,4,3,2,2,1,1], player1=player1, player2=player2)
    # game = game.Game(size = 10, ships = [5])

    game.initialize_game()
    game.print_gamestate()

    while not game.game_over():
        game.one_turn()
                
    return game.winner

        
if __name__ == '__main__':
    play_battleships('MC', 'MC2')