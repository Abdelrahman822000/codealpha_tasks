## Author  : Abdelrahman Mohamed Hamad
## Date    : 4/3/2024
## Version : 1.6.7

#!/usr/bin/env python3

import tkinter as tk
import customtkinter as CTk
import random

def getRandomWord(wordsList):
    # This function returns a random string from the passed list of strings.
    return random.choice(wordsList)

def Init():
    # This function makes the list of Stickman pictures (HANGMAN_PICS) and Stickman when the player win (WIN).
    # And initiates the values of missedLetters,correctLetters with an empty string ("") , and initiates Z with value 1.
    global HANGMAN_PICS,Win,missedLetters,correctLetters,Z,words,z
    # HANGMAN_PICS is a list of constant strings that contains the picture of stickman at each stage
    HANGMAN_PICS = ['''
    +---+
        |
        |
        |
        |
       ===''', '''
    +---+
        |
    O   |
        |
        |
       ===''', '''
    +---+
        |
    O   |
    |   |
        |
       ===''', '''
    +---+
        |
    O   |
   /|   |
        |
       ===''', '''
    +---+
        |
    O   |
   /|\  |
        |
       ===''', '''
    +---+
        |
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
        |
    O   |
   /|\  |
   / \  |
       ===''', '''
    +---+
    |   |
    O   |
   /|\  |
   | |  |
       ===''']
    # Win is a list that contains a constant string that is the stickman when the player wins.
    Win = ['''
    +---+
        |
   \O/  |
    |   |
   / \  |
       ===''']
    missedLetters = ''
    correctLetters = ''
    Z = 1
    z = 0
    words=''

def Initiate(event):
    global title1,title2,title3,title4,title5,title6,title7,title,Var,Var1,String,String1,custom_font,Z
    # This function starts when the player press enter at the first text box.
    # The function takes the value in the first text box and choose a category depending on that value.
    if Z==0:
    # This if statement is to make sure that when the game ends any input won't be used untill the game is restarted. 
        title6.configure(text="Game Ended press Space to reset")
        Var.set("")
        Var1.set("")
        return
    Type=String.get().lower() # Takes the input of the first text box
     
    try:
        # This statement is to make sure that the input is not empty
        if Type ==" ":
            # This if statement is to remove any spaces added to the input as the only input allowed is one character
            title2.configure(text="Error, Enter a character")
            return
        elif Type[0]==" ":
            Type=Type[1:]
    except IndexError:
        title2.configure(text="Error, Enter a character")
        return
    if len(Type)>1:
    # This if statement is to make sure that more than one letter is not allowed in the input
        title2.configure(text="Enter one number only")
        Var.set("")
        return
    global word,correctLetters,missedLetters,l,z
    wordsN  = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred".split()
    wordsA  = "ant bat bear bee camel cat cobra cougar cow coyote crow deer dog donkey duck eagle fox frog goat goose hawk horse lion lizard llama mole monkey moose mouse mule owl panda parrot pig pigeon python rabbit ram rat raven rhino salmon seal shark sheep snake spider swan tiger turkey turtle whale wolf worm zebra".split()
    wordsCo = "blue red yellow green orange black purple white grey brown pink".split()
    wordsCl = "tshirt suit belt pants vest gloves dress skirt shirt jacket scarf shorts tie coat socks".split()
    wordsB  = "eyes teeth toes head eyebrows ears hair shoulder tongue bones hands fingers knee ankle nose legs neck mouth".split()
    # The following if statement is to choose a category
    if Type=='1':
        # Numbers
        words = wordsN
        title7.configure(text="Chosen category: Numbers")
    elif Type == '2':
        # Animals
        words = wordsA
        title7.configure(text="Chosen category: Animals")
    elif Type == '3':
        # Colors
        words = wordsCo
        title7.configure(text="Chosen category: Colors")
    elif Type == '4':
        # Clothes
        words = wordsCl
        title7.configure(text="Chosen category: Clothes")
    elif Type == '5':
        # Body
        words = wordsB
        title7.configure(text="Chosen category: Body")
    elif Type == ' ':
        title2.configure(text="Error, Enter a character")
        return
    else:
        # All categories
        words= wordsN + wordsA + wordsCo + wordsCl + wordsB
        title7.configure(text="Chosen category: All")
    word=getRandomWord(words) # choose a secret word
    l=['_' for x in range(len(word))] # Make a list with length equal to the secret word's length and with all values equal to '_'
    Var.set("")
    title1.configure(text=" ".join(l)) # Print the list 'l'
    z = 1
    return

def Hangman_Game(event):
    global title1,title2,title3,title4,title5,title6,title7,title,Var,Var1,String,String1,custom_font
    # This function starts when the player press enter at the second text box.
    # This function takes the input of the second text box and check if it is in the secret word or not.
    re=""
    global HANGMAN_PICS,Win,word,correctLetters,missedLetters,l,z
    if z==0:
    # This if statement is to make sure that when the game ends any input won't be used untill the game is restarted. 
        title6.configure(text="Game Ended press Space to reset")
        Var.set("")
        Var1.set("")
        return
    # print(f"missedLetters = {missedLetters}")
    # print(f"correctLetters = {correctLetters}")
    # print(f"word = {word}")
    
    #print(" ".join(l))
    Input=String1.get().lower() # Takes the input of the second text box
    try:
        # This statement is to make sure that the category has been chosen first
        title1.configure(text=" ".join(l)) # print list 'l'
    except NameError:
        title2.configure(text="Error, You didn't choose a category")
        return
    try:
        # This statement is to make sure that the input is not empty
        if Input ==" ":
            # This if statement is to remove any spaces added to the input as the only input allowed is one character 
            title2.configure(text="Error, Enter a character")
            return
        elif Input[0]==" ":    
            Input=Input[1:]
    except IndexError:
        title2.configure(text="Error, Enter a character")
        return
    if len(Input)>1:
        title2.configure(text="Enter one letter only") # print "Enter one letter only"
        Var1.set("")
        return
    else:
        title2.configure(text="")
    for i in range(len(word)):
        if Input == word[i] and l[i]=='_':
            l[i]=Input
            if Input in correctLetters:
                pass
            else:
                correctLetters += Input
    if Input in missedLetters:
        pass
    elif Input in correctLetters:
        pass
    else:
        missedLetters += Input
    if '_' not in l:
        title2.configure(text="You Win!") # print "You Win!"
        #print("You Win!")
        title3.configure(text=Win[0],font=custom_font) # print the value if Win[0]
        #print(Win[0])
        word_new="".join(l)
        title4.configure(text="The word is: "+ word_new) # print the secret word
        z=0
        #print("The word is: "+ word_new)
        re= "End"
    if re=="End":
        pass
    else:   
        title3.configure(text=HANGMAN_PICS[len(missedLetters)],font=custom_font) # draw the stickman
        #print(HANGMAN_PICS[len(missedLetters)])
    if(len(missedLetters)==len(HANGMAN_PICS)-1):
        title2.configure(text="You Lost!") # print "You Lost!"
        title4.configure(text="The word was: "+ word) # print the secret word
        z=0
        #print("You Lost!")
    title1.configure(text=" ".join(l)) # print the list 'l'
    Var1.set("")
    return

def Reset(event):
    # This function restarts the game
    global Z,words,word,l,z
    word=''
    words=''
    l=[]
    Z=1
    z=0
    Init()
    title1.configure(text="")
    title2.configure(text="")
    title3.configure(text=HANGMAN_PICS[0],font=custom_font)
    title4.configure(text="")
    title6.configure(text="")
    title7.configure(text="")
    Var.set("")
    Var1.set("")
    return

if __name__ == '__main__':
    Init()

    # System Settings 
    CTk.set_appearance_mode("System")
    CTk.set_default_color_theme("blue")

    # App frame
    app = CTk.CTk()
    app.geometry("1080x720")
    app.title("Hangman Game")

    # Adding UI elements
    # title = CTk.CTkLabel(app, text="Enter a letter \nPress Enter to start \nPress Space to reset")
    # title.pack(padx=10, pady=10)

    title = CTk.CTkLabel(app, text="Enter a number to Choose Category\nPress '1' for Numbers\nPress '2' for Animals\n Press '3' for Colors\n Press '4' for Clothes\n Press '5' for Body\n Otherwise pick all categories\n Then press Enter" )
    title.pack(padx=10, pady=10)

    Var=tk.StringVar()
    String=CTk.CTkEntry(app,width=350, height=40, textvariable=Var)
    String.bind("<Return>", Initiate)
    String.bind("<space>", Reset)
    String.pack(padx=10,pady=10)

    title5 = CTk.CTkLabel(app, text="Enter a letter \nPress Enter to start \nPress Space to reset")
    title5.pack(padx=10, pady=10)

    Var1=tk.StringVar()
    String1=CTk.CTkEntry(app,width=350, height=40, textvariable=Var1)
    String1.bind("<Return>", Hangman_Game)
    String1.bind("<space>", Reset)
    String1.pack(padx=10,pady=10)

    # Operation
    # Button1= CTk.CTkButton(app, text="Start",command=Hangman_Game)
    # Button1.pack(padx=10,pady=10)

    # Button2= CTk.CTkButton(app, text="Reset",command=Reset)
    # Button2.pack(padx=10,pady=10)

    custom_font = CTk.CTkFont(size=20)

    # Printing Output
    title7 = CTk.CTkLabel(app, text="")
    title7.pack(padx=10, pady=10)
    title1 = CTk.CTkLabel(app, text="")
    title1.pack(padx=10, pady=10)
    title2 = CTk.CTkLabel(app, text="")
    title2.pack(padx=20, pady=20)
    title3 = CTk.CTkLabel(app, text=HANGMAN_PICS[0],font=custom_font)
    title3.pack(padx=10, pady=10)
    title4 = CTk.CTkLabel(app, text="")
    title4.pack(padx=10, pady=10)
    title6 = CTk.CTkLabel(app, text="")
    title6.pack(padx=10, pady=10)

    # Run App
    app.mainloop()