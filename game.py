import sys
from typing import List, Any, Dict, Union

from tabulate import tabulate

'''
Game.py class is used to store the game information and contains the logic of the game
'''

class Game :
    ret: List[Any]=[]
    score: float=0.0
    used_letter: List[Any]=[]
    bad_guess: int=0
    missing_letters: int=4
    data_set={'a': 8.17,'b': 1.49,'c': '2.78','d': 4.25,'e': 12.70,'f': 2.23,'g': 2.02,
              'h': 6.09,'i': 6.97,'j': 0.15,'k': 0.77,'l': 4.03,'m': 2.41,'n': 6.75,'o': 7.51,
              'p': 1.93,'q': 0.10,'r': 5.99,'s': 6.33,'t': 9.06,'u': 2.76,'v': 0.98,'w': 2.36,
              'x': 0.15,'y': 1.97,'z': 0.07}
    letter_selected: int=1

    '''
    scoreCalculator is the method used to calculate the result of each game played
    @param expected_word the correct word
    @param before_guess the word before making any attempt by the user
    @param after_guess the word after making an attempt by the user
    @param score1 the current score of the ongoing run
    @param status the status Success or Gaveup for the ongoing run
    '''

    def scoreCalculator(self, expected_word, before_guess, after_guess, score1, status) -> int:
        try:
            if status=="GaveUp":
                for n in range(0, 4):
                    if expected_word[n] == after_guess[n] and before_guess[n] == '-' and after_guess != '-' :
                        score1 = score1 - self.data_set.get ( expected_word[n] )
            else:
                for n in range(0,4):
                    if expected_word[n] == after_guess[n] and before_guess[n] == '-' and after_guess != '-' :
                        score1 = score1 + self.data_set.get(expected_word[n])
        except:
            print("ERRRRR: Something BAD HAPPENED,Dont worry the exception is caught,YOU TRY THE NEXT GAME")
        if score1<0:
            return score1
        return score1/self.letter_selected

    '''
    start method is used to execute the game which is initially called from Guess class
    @:param expected_word the correct word
    @:param actual_word the word given to the user initially and keeps on updating with each user guess
    @:param res the status of the each run
    @:param count the number of games played
    '''

    def start(self, expected_word, actual_word, res, count):
        c: int=0
        for n in range (0,4):
            if actual_word[n]!="-" :
                c += 1
        if c == 4:
            self.ret.append(count), self.ret.append(expected_word), self.ret.append(res),
            self.ret.append(self.bad_guess), self.ret.append(self.missing_letters),
            self.ret.append(self.score)
            return self.ret
        print( actual_word )
        user_response: str=input ( "g = guess, t = tell me, l for a letter, and q to quit\n" )
        if user_response == 't':
            print("Correct answer is : ", expected_word)
            self.score=self.scoreCalculator(expected_word, actual_word, expected_word, self.score, 'GaveUp')
            actual_word = expected_word
            self.start(expected_word,actual_word,'GAVE UP',count)
        elif user_response == 'g':
            user_guess: str=input ( "Enter your guess\n" )
            if (user_guess == expected_word):
                print( "You won\n" )
                self.score=self.scoreCalculator(expected_word, actual_word, user_guess, self.score, 'Win')
                actual_word = user_guess
                self.start(expected_word, actual_word, 'SUCCESS', count)
            else :
                self.bad_guess += 1
                self.score = self.score-(0.1*self.score)
                print( "You lose, try again\n" )
                self.start(expected_word,actual_word,'',count)
        elif user_response == 'l':
            flag: bool=False
            letter_found: int=0
            self.letter_selected += 1
            user_letter: str=input ( "Enter a letter\n" )
            before_word = actual_word
            for n in range(0, 4):
                if actual_word[n] != "-":
                    continue
                if expected_word[n] == user_letter:
                    flag = True
                    letter_found += 1
                    self.missing_letters -= 1
                    s=list(actual_word)
                    s[n]=user_letter
                    actual_word=''.join(s)
            if flag == False:
                self.bad_guess += 1
            print( "You found ", letter_found, " letters" )
            if expected_word==actual_word:
                self.scoreCalculator(expected_word, actual_word, before_word, self.score, 'Last guess')
            self.used_letter.append(user_letter)
            self.start(expected_word, actual_word, '', count)
        elif user_response == 'q' :
            self.show_data( )
            sys.exit("GAME OVER")
        else:
            print("Please enter valid responses, g,t,l or q\n")
            self.start(expected_word, actual_word, '', count)

    '''
    show_data method is used to display the final run results
    '''
    def show_data( self ):
        table_headers = ['Game', 'Word', 'Status', 'Bad Guess', 'Missing Letters', 'Score']
        chunks: List[List[Any]] = [self.ret[x :x+6] for x in range(0, len(self.ret), 6)]
        print(tabulate(chunks, headers = table_headers))
