import re
import tkinter as tk
import customtkinter as ctk
from tkinter.scrolledtext import ScrolledText

import nltk
from nltk.corpus import words

nltk.download('words')

class SpellChecker01(ctk.CTkFrame):
    def __init__(self, master, width=100, height=100, **kwargs):
        super().__init__(master, width, height, **kwargs)
        self.text=ScrolledText(self)

def main():
    """
    Following a spell-checker tutorial while giving my own spin on it.
    Tutorial reference: https://www.youtube.com/watch?v=_nkQd9SyEpw
    :return:
    """

    return


if __name__ == "__main__":
    main()
