from game import Game
from stringDatabase import dataLoader
import os
from tabulate import tabulate


class Guess:
    count = 1
    while count < 100:
        print("** The Great Guess Game **")
        expected_word  = dataLoader.gettingData("..\\COMP_6411\\four_letters.txt")
        Game().start(expected_word, "----", '', count)
        count+=1


# guess.py will be used to run the project
# it will define the outlook and the layout of the project