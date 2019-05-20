from game import Game
from stringDatabase import dataLoader
import os
from tabulate import tabulate


class Guess():
    count = 1
    table_headers = ['Game', 'Word', 'Status', 'Bad Guess', 'Missing Letters', 'Score']
    while count < 3:
        print("** The Great Guess Game **")
        expected_word = "laid"
            # dataLoader.gettingData("..\\COMP_6411\\four_letters.txt")
        Game().start(expected_word, "----", '', count)
        if Game().quit_flag == True:
            count = 4
        count+=1
    # entry.append(Game().ret)
    chunks = [Game().ret[x:x + 6] for x in range(0, len(Game().ret), 6)]
    print(tabulate(chunks, headers=table_headers))

# guess.py will be used to run the project
# it will define the outlook and the layout of the project