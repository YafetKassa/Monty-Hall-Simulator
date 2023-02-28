'''
Visualization of the Monty Hall Simulation results.
'''

import monty_hall
import pandas as pd
import seaborn as sns

class Plot:
    '''
    This class stores the data for a particular instance of a simulation of the monty hall problem. It
    contains functionality to export a visualization of the win percentages.

    Attributes
    • doors: An integer; The number of doors that the simulation will be based on.
    • iterations: An integer; The number of iterations that a simulation will be based on.
    • sequence: A list; Starts empty, is later populated by dictionaries each containing: num of
    iterations a game was played, percentage won for that simulation, doors used in that
    simulation, whether the door was switched or not for that simulation.

    '''

    def __init__(self, doors = 3, iterations = 200):
        '''
        Constructor for Plot Class  

        Parameters:
            ▪ doors - An integer; Defaults to 3; The number of doors that the simulation will be based on.
            ▪ iterations - iterations: An integer; Defaults to 200; The number of iterations that a
            simulation will be based on.
        '''   
        self.doors = doors
        self.iterations = iterations

        # Create an attribute named sequence that will be a list that will eventually 
        # contain dictionaries that we will use to create a dataframe. 
        self.sequence = []
        
        # Write a loop that will run for as many times as the value of iterations. 
        for i in range(1, iterations+1):
            # create an instance of simulation from the monty_hall namespace
            simulation = monty_hall.Simulation(self.doors) 

            # determine the switch value based upon current iteration (odd = False, even = True)  
            switch = i % 2 == 0

            # invoke the play_game method with switch and current iteration
            score = simulation.play_game(switch, i)

            # append parameters and results dictionary object in sequence
            self.sequence.append({'iterations': i, 'percentage': score, 'doors': self.doors, 'switched': switch})

        # call the make_plot method.
        self.make_plot()

    def make_plot(self):
        '''
        This method will use the sequence attribute to create a pandas Dataframe. 
        lmplot method of seaborn in order to create a plot
        '''

        # create dataframe from sequnce list of play game results 
        df = pd.DataFrame(self.sequence)

        # create plot using pandas data frame 
        g = sns.lmplot(x="iterations", y="percentage", hue="switched", data=df)
        
        # generate file name
        filename = f"monty_hall_{self.doors}_{self.iterations}.png"

        # export plot as image to disk
        g.savefig(filename)

if __name__ == '__main__':
    v = Plot(doors=3, iterations=400)