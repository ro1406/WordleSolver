# WordleSolver
My approach to a Wordle solver. Game played on command line.

Wordle.py: 1st Approach was a semi-naive approach assigning a score similar to the Manhattan Distance to each word, devised by myself.

PlayWordle.py: Lets you play wordle on any site/platform and input the colors recieved after each guess it tells you to make. (Use of score from Wordle.py)

More approaches to come soon including probabilistic methods, search trees etc, with different problem formulations.

Word lists from:
https://gist.github.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b
https://gist.github.com/cfreshman/40608e78e83eb4e1d60b285eb7e9732f

    Updates:
PlayWordle.py: Avoids repeated letters in a location already guessed before. Forces relocation of yellow letters.
