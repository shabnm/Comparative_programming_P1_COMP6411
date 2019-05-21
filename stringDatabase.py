import re
import random
from typing import List, Any, TextIO

'''
dataLoader class will include the disk I/O operation and reading data from hashmap
@param  filename contains the file location
@:return object 4 letter word
'''

class dataLoader():

    def gettingData(filename) -> object:
        """

        :rtype: object
        """
        f: TextIO
        with open(filename, "r") as f:
            wordList: List[Any] = re.findall(r"[\w']+", f.read())
            f.close()
            return wordList[random.randint(1,4030)]
