import re
import customtkinter as ctk
from tkinter.scrolledtext import ScrolledText

import nltk
from nltk.corpus import words
from transformers import T5ForConditionalGeneration, T5Tokenizer

from Miniprojects.machine_learning.CTK_themes import DarkMode

nltk.download('words')


def simplified(s:str):
    s2:str=s.lower()
    s3:str=re.sub(r"[^\w]", "", s2)
    return s3


class SpellChecker01(ctk.CTkFrame):
    def __init__(self, master, width=100, height=100, model_name="t5-small", **kwargs):
        super().__init__(master, width, height, **kwargs)
        self.text = ScrolledText(self,width=42,height=42,font=("Agency FB",42))
        self.text.bind("<KeyRelease>", self.check)
        self.text.pack()
        self.old_spaces=0
        self.model_name=model_name

    def check(self,_):
        content=self.text.get(1.0,ctk.END)
        spaces=content.count(' ')
        self.old_spaces=spaces

        for tag in self.text.tag_names():
            self.text.tag_delete(tag)

        curind=0
        for word in content.split():
            subword=simplified(word)
            nexind=curind+len(word)
            if subword not in words.words():
                self.text.tag_add(word, f"1.{curind}",f"1.{nexind}")
                self.text.tag_config(word, foreground="red")
            curind=nexind+1


def main():
    """
    Following a spell-checker tutorial while giving my own spin on it.
    Tutorial reference: https://www.youtube.com/watch?v=_nkQd9SyEpw

    Note: Apparently, "wasps" is not a valid word.
    :return:
    """
    MAIN = DarkMode.get_main()
    schk = SpellChecker01(MAIN, 100, 100)
    schk.pack()
    MAIN.mainloop()
    return


if __name__ == "__main__":
    main()
