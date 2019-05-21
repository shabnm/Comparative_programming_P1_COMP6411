from game import Game
from stringDatabase import dataLoader

'''
Guess.py class is used to run the project
@param count keeps track of number of runs
@param expected_word get random 4 digit word from the four_text.txt
'''


class Guess :
    count: int=1
    '''
    Can execute for 100 runs, select q to stop the run
    '''
    while count < 100:
        print ( "** The Great Guess Game **" )
        expected_word: object=dataLoader.gettingData ( "..\\COMP_6411\\four_letters.txt" )
        Game ( ).start ( expected_word, "----", '', count )
        count += 1
