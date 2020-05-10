import numpy as np
import string
import random
import os

# for usage with jupyter notebook
from IPython.display import clear_output

class Board:

    def __init__(self, size = 10):
        self.size = size
        self.state = np.zeros((size,size), dtype = bool)
        self.observed = np.zeros((size,size), dtype = bool)
        self.ships = []

    def show_board(self, show_all = False):
        show = np.empty((self.size+1, self.size+1), dtype = str)
        #show[1:11,0]= list(string.ascii_uppercase)[:10]
        show[1:11,0]= list(range(0,10))
        show[0,0] = " "
        show[0,1:11]= list(range(0,10))
        for i in range(self.size):
            for j in range(self.size):
                if self.observed[i,j] or show_all:
                    if self.state[i,j] == 1:
                        show[i+1,j+1]= "X"
                    else:
                        show[i+1,j+1] = "."
                else:
                    show[i+1,j+1] = "-"
        return show

    def place_ship(self,i,j,l,h):
        """
        i: i-coordinate of ship
        j: j-coordinate of ship
        l: length of ship
        h: horizontal = True, vertical = False
        """
        if not h:
            if i+l <= self.size and (self.state[i:i+l,j]==0).all() and j < self.size:
                self.state[i:i+l,j] = 1
                self.ships.append((i,j,l,h))
            else:
                raise ValueError("invalid position!")
        else:
            if j+l <= self.size and (self.state[i,j:j+l]==0).all() and i < self.size:
                self.state[i,j:j+l] = 1
                self.ships.append((i,j,l,h))
            else:
                raise ValueError("invalid position!")

    def observe(self,i,j):
        if i < self.size and j < self.size and not self.observed[i,j]:
            self.observed[i,j]= True
            sunken_ship = None
            for ship in self.ships:
                i1,j1,l,h = ship
                if h and (self.observed[i1,j1:j1+l]==1).all():
                    self.ships.remove(ship)
                    sunken_ship = ship
                    break
                elif (not h) and (self.observed[i1:i1+l,j1]==1).all():
                    self.ships.remove(ship)
                    sunken_ship = ship
                    break
            return self.state[i,j], sunken_ship
        else:
            raise ValueError("invalid observation!")

    def random_initialization(self, ships):
        """
        randomly place ships with lengths as specified in list ships
        """
        for l in ships:
            placed = False
            while not placed:
                # horizontal or vertical
                h = random.choice([True, False])
                if h:
                    # horizontal
                    i = random.randint(0,self.size-1)
                    j = random.randint(0,self.size-l-1)
                    if (self.state[i,j:j+l]==0).all():
                        self.state[i,j:j+l] = 1
                        self.ships.append((i,j,l,h))
                        placed = True
                else:
                    # vertical
                    i = random.randint(0,self.size-l-1)
                    j = random.randint(0,self.size-1)
                    if (self.state[i:i+l,j]==0).all():
                        self.state[i:i+l,j] = 1
                        self.ships.append((i,j,l,h))
                        placed = True

    def manual_initialization(self,ships):
        """
        ask user where to place the ships.
        """
        for l in ships:
            
            error = False

            while True:
                try:
                    # clear output
                    cls()
                    clear_output(wait=True)
                    
                    if error:
                        print("Oops!  Invalid Position.  Try again...")
                        error = False
                    
                    print("Please place your ship of length "+str(l)+". Your board state is:")
                    show = self.show_board(show_all=True)
                    for line in show:
                        print(*line)
                    i = input('Enter i-coordinate: ')
                    j = input('Enter j-coordinate: ')
                    orient = input('Enter orientation (h=horizontal, v=vertical): ')
                    if orient == "h":
                        h = True
                    elif orient == "v":
                        h = False
                    else:
                        raise ValueError("Orientation parameter has to be h or v.")

                    self.place_ship(int(i),int(j),l,h)
                    
                    break
                    
                except ValueError:
                    error = True
                

        print("Placement of ships finished.")
        
        
        
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
