**This Game was developed by Abdelrahman Mohamed Hamad**

#About Hangman Game:

it is a word-guessing game.
The player chooses a category, a secret word is randomly picked from the selected category,
then the player tries to guess the secret word. 

When the player guesses a letter that isn't in the word, 
the game draws part of a stickman for each wrong guess.

When the player guesses a letter that is in the word,
the letter is assigned to its location and the game continues.

If the drawing of the stickman is completed then he will be hanged and the player loses.

If the player guesses the secret word right before the drawing is completed he wins and the stickman is saved.



#Insructions:

To Run the game just open "Hangman Game.exe"

If you have Python you can check the code in "Hangman_Game.py"

First, check that you have "tkinter" and "customtkinter" libraries downloaded

If the libraries aren't downloaded you can download them by typing this commands in the terminal:
pip install tkinter
pip install customtkinter

#How to play:

After opening the game you will have two text boxes to type in

The first text box: you choose the category you wish to have from
(Numbers, Animals, Colors, Clothes, Body) or choose all of them.
    if you type: 
		-'1': Numbers
		-'2': Animals
		-'3': Colors
		-'4': Clothes
		-'5': Body
		-Otherwise: All categories

After choosing the category, the game will randomly select a secret word from the chosen category.

The second text box: you type a letter and press enter

if the letter is in the secret word, it is assigned to its location and the game continues.

if the letter isn't in the secret word, the game draws a part of a stickman and the game continues.

the game continues until all letters are guessed right, in this case, you win, 
or until the drawing of the stickman is completed, in this case, you lost.

After finishing the game you can press space to reset.
