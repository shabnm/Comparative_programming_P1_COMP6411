# will include the disk I/O operation, reading data from hashmap
import re
import random


class dataLoader():

    def gettingData(filename):
        with open(filename, "r") as f:
            wordList = re.findall(r"[\w']+", f.read())
            f.close()
            return wordList[random.randint(1,4030)]

