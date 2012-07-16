# -*- coding: cp1252 -*-
from Tkinter import *
import tkMessageBox

class App:
    def __init__(self, master):
        container = Frame(master)
        container.pack(fill=BOTH, expand=1)

        self.plain_frame = Frame(container)
        self.plain_frame.pack(side=LEFT, fill=BOTH, expand=1)

        self.key_frame = Frame(container)
        self.key_frame.pack(side=LEFT, fill=BOTH, expand=1)

        self.cypher_frame = Frame(container)
        self.cypher_frame.pack(side=LEFT, fill=BOTH, expand=1)
        
        # Alphabet Frame
        self.alpha_frame = Frame(master)
        self.alpha_frame.pack(side=BOTTOM)
        self.alphabet_text = Text(self.alpha_frame, height=2, width=60)
        self.alphabet_text.insert(END, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,?!@\/|;'#:~[]{}_+-=()*&^%$<>")
        #self.alphabet_text.config(state=DISABLED)
        self.alphabet_text.pack(side=RIGHT)
        self.alpha_label = Label(self.alpha_frame, text="Alphabet")
        self.alpha_label.pack(side=LEFT)
        
        # Encrypt button 
        self.encrypt_btn = Button(self.plain_frame, text="Encrypt -->", command=self.do_encrypt)
        self.encrypt_btn.pack(side=BOTTOM)

        # Decrypt button
        self.decrypt_btn = Button(self.cypher_frame, text="<-- Decrypt", command=self.do_decrypt)
        self.decrypt_btn.pack(side=BOTTOM)

        # Plaintext
        self.plain_label = Label(self.plain_frame, text="Plaintext")
        self.plain_label.pack()
        self.plain = Text(self.plain_frame, width=20, height=20)
        self.plain.pack(fill=BOTH, expand=1)
        
        # key
        self.key_label = Label(self.key_frame, text="Key")
        self.key_label.pack(side=TOP)
        self.key = Text(self.key_frame, width=20, height=20)
        self.key.pack(fill=BOTH, expand=1)


        # cypher
        self.cypher_label = Label(self.cypher_frame, text="Cypher")
        self.cypher_label.pack()
        self.cypher = Text(self.cypher_frame, width=20, height=20)
        self.cypher.pack(fill=BOTH, expand=1)

    def do_encrypt(self):
        self.populate_alphabet()
        plain = self.plain.get(1.0, END)
        key = self.key.get(1.0, END)
        length = len(plain) - 1
        cypher = ""
        
        self.cypher.delete(1.0, END)
        
        for x in range(length):             # for each character:
            pnum = self.find_num(plain[x]) # plaintext as number
            try:
                knum = self.find_num(key[x])   # key as number
            except IndexError:
                self.show_error("Oops", "Key was too short.")
                return 0
            cnum = (pnum + knum) % len(self.letters_list)    # cypher as number
            cletter = self.letters_list[cnum]                # cypher as letter
            self.cypher.insert(END, cletter)

    def do_decrypt(self):
        self.populate_alphabet()
        cypher = self.cypher.get(1.0, END)
        key = self.key.get(1.0, END)
        plain = ""
        length = len(cypher) - 1
        self.plain.delete(1.0, END)
        
        for x in range(length):
            cnum = self.find_num(cypher[x])
            knum = self.find_num(key[x])
            pnum = (cnum - knum) % len(self.letters_list)
            pletter = self.letters_list[pnum]
            self.plain.insert(END, pletter)

    def show_error(self, title, message):
        tkMessageBox.showinfo(title, message)

    def populate_alphabet(self):
        self.letters_list = list(self.alphabet_text.get(1.0, END))

    def find_num(self, search_str):
        for z in range(len(self.letters_list)):
            if self.letters_list[z] == search_str:
                return z
        
root = Tk()
root.wm_title("Onetime")
app = App(root)
root.mainloop()
