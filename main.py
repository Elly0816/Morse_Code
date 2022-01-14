import ast

import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

class Morse:
    
    def __init__(self, raw_string):
        self.string = raw_string
        self.morse_codes = {}

    def create_file(self):
        URL = 'http://www.sckans.edu/~sireland/radio/code.html'
        # Fetch the tables from the website to populate a dictionary
        soup = BeautifulSoup(requests.get(URL).text, 'html.parser')
        table = soup.find_all('table')
        
        # #TODO 1: ADD THE LETTERS INTO THE DICTIONARY
        letter_table = table[0].find_all('tr')[1:]
        for row in letter_table:
            letters = row.find_all('td')[0].text.strip().lower()
            morse = row.find_all('td')[1].text.strip()
            self.morse_codes[letters] = morse
        # print(self.morse_codes)
        
        # #TODO 2: ADD THE NUMBERS INTO THE DICTIONARY
        number_table = table[1].find_all('tr')[1:]
        for row in number_table:
            numbers = row.find_all('td')[0].text.strip()
            morse = row.find_all('td')[1].text.strip()
            self.morse_codes[numbers] = morse
        # pprint(self.morse_codes)
        
        # #TODO 3: ADD PUNCTUATIONS AND SPACES INTO THE DICTIONARY
        punctuations = {'.': '*_ *_*_',
                        ',': '__**__',
                        '?': '**__**',
                        ';': '_*_*_*',
                        ':': '___***',
                        '-':'_****_',
                        '/':'_**_*',
                        "'":'*____*',
                        '"':'*_**_*',
                        "!": '_._.__'}
        for key in punctuations:
            self.morse_codes[key] = punctuations[key]
        
        for key in self.morse_codes.keys():
            self.morse_codes[key] = self.morse_codes[key].replace('*', '.')
        

        ## TODO 3: WRITE THE DICTIONARY TO A FILE
        
        with open('morse_code.txt', 'w') as morse_file:
            morse_file.write(json.dumps(self.morse_codes))

    def convert(self):
        self.create_file()
        ## TODO 4: ASK THE USER FOR INPUT
        with open('morse_code.txt', 'r') as morse_file:
            morse_string = ""
            morse_code = json.load(morse_file)
            # print(morse_code)
            for word in self.string:
                for letter in word:
                    if letter in morse_code.keys():
                        morse_string += f"{morse_code[letter]}   "
                    else:
                        pass
                morse_string += "   /   "
        return morse_string


print('This is a text to morse converter')
to_convert = input('Enter what you want to convert to morse code:\n').lower().split()

morse = Morse(raw_string=to_convert)
print(morse.convert())
man = input('')