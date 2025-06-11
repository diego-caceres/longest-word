# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import string
import random
import requests

class Game:
    """
    The Longest Word:
    a game where given a list of nine letters,
    you have to find the longest possible English word formed by those letters
    """
    def __init__(self) -> list:
        """Attribute a random grid of size 9"""
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))
        #print(self.grid)

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False

        return self.__check_dictionary(word)

    @staticmethod
    def __check_dictionary(word):
        # Call the API to check if word is valid
        response = requests.get(f"https://dictionary.lewagon.com/{word}")
        json_response = response.json()
        print(json_response)
        return json_response['found']

if __name__ == '__main__':
    game = Game()
    game.grid = list('TOAMFTO') # Force the grid to a test case:
    result = game.is_valid('TOMATO')
    print(result)
