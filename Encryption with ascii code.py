# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 15:31:29 2023

@author: Acer
"""

from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Encrytion with Ascii Code")
root.configure(background = "blue")

entry_word = Entry(root)
entry_word.place(relx=0.5,rely=0.6,anchor = CENTER)
label_1 = Label(root, text = " Name in Ascii: ", bg = "cyan" , fg = "black")
label_2 = Label(root, text = " Name in Character Code: ", bg = "green" , fg = "beige")

def Asciiconverter():
    
    input_word = str(entry_word.get())
    
    for letter in input_word:
        label_1["text"] += str(ord(letter))+  " "
        ascii = int(ord(letter))
        encrypted = ascii - 1
        print(encrypted)
        label_2["text"] += str(chr(encrypted))+ " "
        
btn1 = Button(root, text = "Generate Ascii and Character Code", command = Asciiconverter)
btn1.place(relx = 0.5, rely = 0.7, anchor = CENTER)
label_1.place(relx = 0.5, rely = 0.8, anchor = CENTER)
label_2.place(relx = 0.5, rely = 0.9, anchor = CENTER)

root.mainloop()