import random
import copy
import numpy as np

class HumanAgent:

    def __init__(self):
        pass

    def select_observation(self):
        i = input('Enter i-coordinate: ')
        j = input('Enter j-coordinate: ')
        return int(i),int(j), None

    def update_observations(self,i,j,observation, sunken_ship):
        pass
