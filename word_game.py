import json
from itertools import permutations
from typing import List, Dict, Tuple, Union

from exception_handler import EmptyDictionary, EmptyWordList



class WordGame:
    def __init__(self):
        self.game_started = False
        self.dictionary: Dict[str, int] = {}
        
    def set_values(self, letters: str, length: int = None):
        self.letters = letters
        self.length = length
        self.words_list: List[str] = []
        
    def permutate_words(self):
        words_list: List[str] = [] 
        for iterable in permutations(self.letters, self.length):
            word = "".join(iterable)
            words_list.append(word.lower())
        self.words_list = words_list
    
    def open_dictionary(self):
        with open('words_dictionary.json', 'r') as dictionary_file:
            dictionary = json.load(dictionary_file)
            self.dictionary = dictionary
            
    def find_valid_words(self) -> List[str]:
        if not self.words_list:
            raise EmptyWordList("You must call the instance method 'permutate_words' first.")
        
        if not self.dictionary:
            raise EmptyDictionary("You must call the instance method 'open_dictionary' first.")
        valid_english_words: List[str] = []
        for word in self.words_list:
            if self.dictionary.get(word):
                valid_english_words.append(word)
        return sorted(valid_english_words)
    
    def game_intro(self):
        print("Welcome to the word cross hack!")
        print("How to play:")
        print("Enter the letters and we will display all possible english words that can be formed from that set of letters")
        print("if you wish to restrict the length of each word displayed, type the letters and the length separated by a hyphen like this: father-5")
        print("On the next prompt enter the letters")
        self.game_started = True
    
    @staticmethod
    def extract_values(input_data_str: str) -> Tuple[str, Union[int, None]]:
        # retrieve letters and length
        input_data: List[str] = input_data_str.split(sep="-")
        if len(input_data) > 1:
            letters, length = input_data
            length = int(length)
        else:
            letters = input_data[0]
            length = None
        return letters, length

    def play(self):
        while True:
            # display intro message if its the first loop
            not self.game_started and self.game_intro()
            input_data: str = input("Please type the letters: ")
            letters, length = WordGame.extract_values(input_data)
            self.set_values(letters, length=length)
            self.permutate_words()
            words = self.find_valid_words()
            
            print("Here are the valid English words we could suggest:")
            print(">" * 50)
            print(words)
            print(">" * 50)


if __name__ == '__main__':
    game = WordGame()
    game.open_dictionary()
    game.play()

    