import numpy as np
import random

from board import Board, cls
from MC_agent import MCAgent
from human_agent import HumanAgent
from random_agent import RandomAgent

import matplotlib.pyplot as plt
import time

# for usage with jupyter notebook
from IPython.display import clear_output

class Game:

    def __init__(self, size, ships, nb_samples = 1000,
                 player1 = "human", player2 = "random"):
        self.board_player1 = Board(size)
        self.board_player2 = Board(size)
        self.size = size
        self.ships = ships


        if player1 == "human":
            self.player1 = HumanAgent()
        elif player1 == "MC":
            self.player1 = MCAgent(ships = ships,
                                           size = size,
                                           nb_samples = nb_samples)
        elif player1 == "MC2":
            self.player1 = MCAgent(ships = ships,
                                           size = size,
                                           nb_samples = nb_samples)
        else:
            self.player1 = RandomAgent(size = size)

        if player2 == "human":
            self.player2 = HumanAgent()
        elif player2 == "MC":
            self.player2 = MCAgent(ships = ships.copy(),
                                   size = size,
                                   nb_samples = nb_samples)
        elif player2 == "MC2":
            self.player2 = MCAgent(ships = ships.copy(),
                                           size = size,
                                           nb_samples = nb_samples)
        else:
            self.player2 = RandomAgent(size = size)
            

    def print_gamestate(self):
        # clear output before the next move is printed.
        #cls()
        #clear_output(wait=True)

        show = np.empty((self.size+1, 2*(self.size+1)+3), dtype = str)
        show_player2 = self.board_player2.show_board()
        show_player1 = self.board_player1.show_board()
        show[0:self.size+1,0:self.size+1] = show_player2
        show[0:self.size+1,self.size+4:2*(self.size+1)+3] = show_player1
        print("")
        print("Player1's observations"+" "*3+"Player2's observations")
        print("")
        for line in show:
            print(*line)

    def initialize_game(self):
        # if isinstance(self.player1, HumanAgent):
        #     self.board_player1.manual_initialization(self.ships)
        # else:
        self.board_player1.random_initialization(self.ships)
        # if isinstance(self.player2, HumanAgent):
        #     self.board_player2.manual_initialization(self.ships)
        # else:
        self.board_player2.random_initialization(self.ships)

    def one_turn(self):
        print("Enter the coordinates of your next observation:")
        while True:
            try:
                i,j,scores1 = self.player1.select_observation()
                observation, sunken_ship = self.board_player2.observe(i,j)
                if not sunken_ship is None:
                    i1,j1,l,h = sunken_ship
                    print("Player 1 player has sunk ship at ("+str(i1)+","+str(j1)+") with length "+str(l)+"!")
                break
            except:
                print("Player 1 - Invalid observation. Try again.")
        self.player1.update_observations(i,j,observation,sunken_ship)
        while True:
            try:
                # handles the case i or j are empty
                i,j, scores2 = self.player2.select_observation()
                observation, sunken_ship = self.board_player1.observe(i,j)
                if not sunken_ship is None:
                    i2,j2,l,h = sunken_ship
                    print("Player 2 has sunk ship at ("+str(i2)+","+str(j2)+") with length "+str(l)+"!")
                break
            except:
                print("Player 2- Invalid observation. Try again.")
        self.player2.update_observations(i,j,observation,sunken_ship)
        clear_output(wait=True)
        self.print_gamestate()
        # cls()
        # input()


    def game_over(self):
        if self.board_player2.ships == []:
            if self.board_player1.ships == []:
                print("Game over! It's a draw!")
                self.winner = None
                return True
            else:
                print("Game over! Player 1 won!")
                self.winner = True
                return True
        elif self.board_player1.ships == []:
            print("Game over! Player 2 won!")
            self.winner = False
            return True
        return False
