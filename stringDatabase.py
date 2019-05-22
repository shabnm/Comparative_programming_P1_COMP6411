"""
dataLoader class will include the disk I/O operation and reading data from hashmap
:param : filename contains the file location
"""

import re
import random
from typing import List, Any, TextIO

class dataLoader():

    def gettingData(filename) -> object:
        """
        getting data takes filename as input and return random 4 digit word from the file
        :return: random 4 digit letter
        :rtype: String
        """
        f: TextIO
        with open(filename, "r") as f:
            wordList: List[Any] = re.findall(r"[\w']+", f.read())
            f.close()
            return wordList[random.randint(1,4030)]
