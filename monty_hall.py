'''
A simulation of the famous Monty Hall Problem.
'''

from random import randrange, choice

class Simulation:
    def __init__(self, numdoors):
        '''
        Set an attribute named numdoors that will be the number of doors that will be used to
        play the game.
        
        Parameters:
            ▪ doornum - An integer; the number of doors that will be used to play the game.
        
        Returns:
            None
        '''

        # make sure we have doors greater than zero
        assert numdoors > 0

        # initialize number of doors used to play the game
        self.numdoors = numdoors
    
    def set_random_doors(self):
        '''
         Create a list of numdoors length containing “zonk” strings. 
         Replace one of those items in the list to the string “car” at random. 
         Returns the list. 
        '''
        # create the list doors with zonk string 
        doors = ['zonk']*self.numdoors

        # randomly place string 'car' in one of the door
        doors[randrange(self.numdoors)] = 'car'
        
        # returns the list
        return doors
    
    def choose_doors(self):
        '''
        Get list from set_random_doors(). 
        Pick and remove a random item from the this list which represents the door that the user/contestant has chosen. 
        Remove first zonk from the list. 
        Pick and remove a random door from the list as the alternate door. 
        Return the contestant door and the alternate door in that order as a tuple.
        '''

        # Get list from set_random_doors(). 
        doors = self.set_random_doors()
        
        # Pick and remove a random item from the this list which represents the door that the user/contestant has chosen. 
        contestant = choice(doors)
        doors.remove(contestant)
        
        # Remove first zonk from the list. 
        if 'zonk' in doors:
            doors.remove('zonk')
        
        # Pick and remove a random door from the list as the alternate door. 
        alternate = choice(doors)
        
        # Return the contestant door and the alternate door in that order as a tuple.
        return(contestant, alternate)

    
    def play_game(self, switch=False, iterations=1):
        '''
        The purpose of this method is to return the percentage of the amount of times that the
        game was won as a decimal (float). 
        
        Parameters:
            
            ▪ switch - A boolean; Default value of False; Determines whether a contestant decides to
            switch their door when playing the game and given the option to do so.

            ▪ iterations - An integer; Default value of 1; The number of times that a person will play
            the game.

        Returns:
            
            decimal (float): the percentage of the amount of times that the game was won

        '''
        # ensure iterations are greater than 0
        assert iterations > 0

        # initialize wins with 0
        wins = 0

        # run the iterations 
        for i in range(iterations):
            
            # choose the doors
            doors = self.choose_doors()
            
            # check if user wins
            if (doors[0] == 'car' and not switch) or (doors[1] == 'car' and switch):
                wins += 1

        # return wins percentage over iterations
        return wins/iterations

if __name__ == '__main__':
    sim = Simulation(3)
    score = sim.play_game(False, 200)
    print(score)