"""
Guess.py class is used to run the project
"""

from game import Game
from stringDatabase import dataLoader

class Guess :
    count: int=1
    while count < 100:
        print ( "** The Great Guess Game **" )
        expected_word: object= dataLoader.gettingData ( "..\\COMP_6411\\four_letters.txt" )
        Game( ).start ( expected_word, "----", '', count )
        count += 1
