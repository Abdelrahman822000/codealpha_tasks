## Author  : Abdelrahman Mohamed Hamad
## Date    : 25/3/2024
## Version : 1.5.3

from os import listdir,remove
from random import choice
from shutil import copy2
import customtkinter as CTk
from tkinter import scrolledtext

# Thanos Project
# This project repeat the operation of the termination of half the population of the universe each time thanos snaps his finger 
def Thanos(x='universe',y='backup'):
    # This function Deletes half of the files randomly 
    l1=listdir('./Thanos/'+x)
    if (len(l1)//2)>=1:
        title1.insert(CTk.END,'Population='+str(len(l1))+'\n')
        title1.insert(CTk.END,'half population='+str(len(l1)//2)+'\n')
        for i in range(len(l1)//2):
            n1=choice(l1)
            remove('./Thanos/'+x+'/'+n1)
            l1.remove(n1)
            title1.insert(CTk.END,'done kill('+n1+')\n')
    elif (len(l1)//2)<1 and len(l1)!=0:
        title1.insert(CTk.END,'half population='+str(len(l1)/2)+'\n')
        for i in range(round(len(l1))):
            n1=choice(l1)
            remove('./Thanos/'+x+'/'+n1)
            l1.remove(n1)
            title1.insert(CTk.END,'done kill('+n1+')\n')
    else:
        title1.insert(CTk.END,'Universe terminated\n')

def copy_imgs(x='universe',y='backup'):
    # This function Restores images from backup
    l2=listdir('./Thanos/'+y)
    for i in range(len(l2)):
        copy2('./Thanos/'+y+'/'+l2[i],'./Thanos/'+x)
    title1.insert(CTk.END,'Universe is restored\n')

def run():
    # This function starts the termination.
    Thanos('universe','backup')

def reset():
    # This function resets the universe.
    copy_imgs('universe','backup')

if __name__ == '__main__':
    # System Settings 
    CTk.set_appearance_mode("System")
    CTk.set_default_color_theme("blue")

    # App frame
    app = CTk.CTk()
    app.geometry("1080x720")
    app.title("Thanos")
    
    # Adding UI elements
    custom_font = CTk.CTkFont(size=20, family="Arial")

    title = CTk.CTkLabel(app, text="Thanos: I finally have all the infinity stones now i can eliminate half of the universe",font=custom_font)
    title.pack(padx=20, pady=20)
    
    Button1= CTk.CTkButton(app, text="Start",command=run)
    Button1.pack(padx=10,pady=10)

    Button2= CTk.CTkButton(app, text="Reset",command=reset)
    Button2.pack(padx=10,pady=10)
    # Printing Output
    custom_font1 = CTk.CTkFont(size=40, family="Arial")

    title1 = scrolledtext.ScrolledText(app, wrap=CTk.WORD, width=40, height=10,fg="white",bg="gray18",font=custom_font1)
    title1.pack(expand=True, fill='both')

    # Run App
    app.mainloop()