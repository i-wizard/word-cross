## Welcome to the Word Cross game hack
This repository contains the python hack to getting correct answers to the word cross game

# Dependecies:
python version `3.xx` installed in your laptop

# Steps to use it
Clone repo
```bash
git clone git@github.com:i-wizard/word-cross.git
```
enter into the project directory
```bash
cd word-cross
```
start game
```
python3 word_game.py
```
###### sample view
```bash
Welcome to the word cross hack!
How to play:
Enter the letters and we will display all possible english words that can be formed from that set of letters
if you wish to restrict the length of each word displayed, type the letters and the length separated by a hyphen like this: father-5
On the next prompt enter the letters
Please type the letters: 
```
Go ahead and type in the random letters and the program will generate a sorted list of valid english words that can be formed with that letter. E.g generate all possible Enlish words from the letter 'quiet'.
```bash
Please type the letters: quiet
Here are the valid English words we could suggest:
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
['quiet', 'quite']
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
```
#### NOTE: 
The length of words generated will be same as the length of letters entered. If you wish to get words with a different length then type the letter and the length you want separated by a hyphen E.g
```bash
Please type the letters: quiet-3
Here are the valid English words we could suggest:
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
['que', 'qui', 'tie', 'tiu', 'tue', 'tui', 'uit', 'ute', 'uti']
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
```
this generated all possible English words from the letter 'quiet' that is 3 characters long.

### Continuity:
This program is like a REPL, so you can just keep typing letters and getting suggestions without needing to manually run the script everytime.

### End Game:
Press `ctr + c` to quit the game.


##### Author:
i-wizard (njoagwuanidavid@gmail.com)