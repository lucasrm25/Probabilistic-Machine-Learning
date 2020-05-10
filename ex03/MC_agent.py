import random
import copy
import numpy as np

def fitShipRandom(board_sample, ship, hit, size):
    possiblePositions = []
    # 1.1 horizontal
    for j in range( hit[1]-ship+1, hit[1]+1 ):
        i = hit[0]
        if j>=0 and j <= size-ship:
            tmp_ship = board_sample[i,j:j+ship]
            if np.all( [valid in [0,1] for valid in tmp_ship] ):
                possiblePositions.append( (i,j,'h') )
    # 1.2 vertical
    for i in range( hit[0]-ship+1, hit[0]+1 ):
        j = hit[1]
        if i>=0 and i <= size-ship:
            tmp_ship = board_sample[i:i+ship,j]
            if np.all( [valid in [0,1] for valid in tmp_ship] ):
                possiblePositions.append( (i,j,'v') )
    # 1.3 check if ship fits
    if np.size(possiblePositions)==0:
        return 0

    # 1.3 randomize valid ship position
    ship_placed = np.random.permutation(possiblePositions)[0]
    if ship_placed[2] == 'v':
        board_sample[ int(ship_placed[0]):int(ship_placed[0])+ship, int(ship_placed[1]) ] = 2
    else:
        board_sample[ int(ship_placed[0]), int(ship_placed[1]):int(ship_placed[1])+ship ] = 2
    
    return 1

class MCAgent:

    def __init__(self, ships, size, nb_samples = 1000):
        self.nb_samples = nb_samples
        self.observed_board = np.zeros((size,size))
        self.remaining_ships = ships
        self.size = size

    def select_observation(self):
        """
        --------------------------------------------------
        THIS IS THE MONTE CARLO SAMPLER YOU NEED TO ADAPT.
        --------------------------------------------------
        
        Select the next location to be observed
        :returns: i_new: int, j_new: int
        """
        
        #  +----------+
        #  |  Task 1  |
        #  +----------+
        # Check if there is already an "open" hit, i.e. a ship that has been hit but not sunk
        # These locations are handled by the observation_board as 1
            
        #  +------------+
        #  |  Task 1a)  |
        #  +------------+
        # If there is already a hit, choose a random one to deal with next.
        # Create a score board including that hit, and reduce the number of samples to 1/10

        #  +----------+
        #  |  Task 2  |
        #  +----------+
        # Populate the score_board with possible boat placements
        
        #  +----------+
        #  |  Task 3  |
        #  +----------+
        # Having populated the score board, select a new position by choosing the location with the highest score.
        
        '''
        Here is how to proceed:

        Hence, to render the problem tractable, we need to approximate the posterior over hits 
        given hit/miss observations. We achieve this through Monte Carlo sampling. Instead of 
        enumerating all board states, we randomly sample nb_samples valid board states (i.e. 
        configurations of ship arrangements on the board) and use their sum to estimate the posterior.
        
        1. Check if there is an "open" hit, i.e. a hit that does not belong to a sunk ship. 
        If so, reduce the number of samples (e.g. to a tenth) and force possible boats to pass 
        through the hit(s) 
        
        2. In case there is no open hit, simulate nb_samples boats, the location and orientation 
        of which are chosen at random. Track them using the score_board. 
        
        3. Find the location with the largest score and return its indices.

        The goal of this assignment is to write such a Monte Carlo sampler.
        '''

        # New board to collect the states sampled by the MC agent
        score_board = np.zeros_like(self.observed_board)

        nb = 0
        while True:
            
            board_sample = self.observed_board.copy()
            remaining_ships = np.random.permutation( self.remaining_ships )
            

            isvalid = True
            for ship in remaining_ships:

                openhits = np.random.permutation(np.stack(np.where(board_sample==1)).T)
                
                # if there is an open hit, place a random ship on that hit
                if np.size(openhits) > 0:
                    hit = openhits[0]
                    if not fitShipRandom(board_sample, ship, hit, self.size):
                        isvalid = False
                        break

                # randomize ship position, since there are no open hits left
                else:
                    unobserveds = np.random.permutation(np.stack(np.where(board_sample==0)).T)

                    foundPosition = False
                    for newhitcenter in unobserveds:
                        foundPosition = fitShipRandom(board_sample, ship, newhitcenter, self.size)
                        if foundPosition:
                            break
                    if not foundPosition:
                        isvalid = False
                        break

            if not isvalid:
                continue
            
            score_board[ np.where(board_sample==2) ] += 1
            nb += 1

            if nb==self.nb_samples: 
                break
        
        score_board[ np.where( self.observed_board == 1 ) ] = 0
        
        # return the next location to query, i_new: int, j_new: int  
        i_new, j_new = np.unravel_index(score_board.argmax(), score_board.shape)
        print(f"\nShooting position {i_new},{j_new}\n")
        return i_new, j_new, score_board


    def update_observations(self, i, j, observation, sunken_ship):
        """
        i:
        j:
        observation:
        """
        if observation:
            self.observed_board[i,j] = 1
        else:
            self.observed_board[i,j] = -1
        if not sunken_ship is None:
            i,j,l,h = sunken_ship
            self.remaining_ships.remove(l)
            if h:
                self.observed_board[i,j:j+l] = -1
            else:
                self.observed_board[i:i+l,j] = -1
