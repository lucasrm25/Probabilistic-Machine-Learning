import random
import copy
import numpy as np

class RandomAgent:

    def __init__(self, size):
        self.observed_board = np.zeros((size,size), dtype = bool)
        self.size = size

    def select_observation(self):
        while True:
            i = random.randint(0,self.size-1)
            j = random.randint(0,self.size-1)
            if not self.observed_board[i,j]:
                return i,j, None

    def update_observations(self,i,j,observation, sunken_ship):
        self.observed_board[i,j] = True
