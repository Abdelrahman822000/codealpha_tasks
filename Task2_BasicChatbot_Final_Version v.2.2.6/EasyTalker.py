## Author  : Abdelrahman Mohamed Hamad
## Date    : 19/3/2024
## Version : 2.2.6

#!/usr/bin/env python3

import customtkinter as CTk
from tkinter import scrolledtext
from Pairs import pairs
import random

class Chat:
    # This class is the main class for the chatbot that contains all its variables and functions.
    def __init__(self,pairs):
        # Initialize self._pairs with the value of pairs.
        self._pairs = pairs
    
    def respond(self,S):
        # This function is to check if the question given have a response or not.
        for (pattern, response) in self._pairs:
            # This loop is to check if the question given have a response or not.
            match = S.lower() in pattern
            if match:
                resp = random.choice(response)
                return resp
            else:
                for question in pattern:
                    if question.lower() in S.lower():
                        resp = random.choice(response)
                        return resp

    def converse(self):
        # This function takes the question of the user as an input and print the response of the chatbot.
        try:
            user_input = String.get().lower()
        except EOFError:
            pass
        response = self.respond(user_input)  # Get the response of the given question
        if response:
            # This if condition check if there is a response or not.
            title1.insert(CTk.END,f"You: {user_input}\nEasyTalker: {response}\n")
        else:
            title1.insert(CTk.END,f"You: {user_input}\nEasyTalker: I'm sorry, I didn't understand.\n")
        String.delete(0, "end") # Empty the textbox.

def run(event):
    # This function Runs the Chatbot.
    EasyTalker = Chat(pairs)
    EasyTalker.converse()

if __name__ == '__main__':

    # System Settings 
    CTk.set_appearance_mode("System")
    CTk.set_default_color_theme("blue")

    # App frame
    app = CTk.CTk()
    app.geometry("1080x720")
    app.title("EasyTalker: a Basic Chatbot")
    
    # Adding UI elements
    custom_font = CTk.CTkFont(size=20, family="Arial")

    title = CTk.CTkLabel(app, text="EasyTalker: Hello there, feel free to chat with me!",font=custom_font)
    title.pack(padx=20, pady=20)
    
    String=CTk.CTkEntry(app,width=350, height=40,font=custom_font)
    String.bind("<Return>", run)
    String.pack(padx=20,pady=30)

    # Printing Output
    custom_font1 = CTk.CTkFont(size=40, family="Arial")

    title1 = scrolledtext.ScrolledText(app, wrap=CTk.WORD, width=40, height=10,fg="white",bg="gray18",font=custom_font1)
    title1.pack(expand=True, fill='both')

    # Run App
    app.mainloop()