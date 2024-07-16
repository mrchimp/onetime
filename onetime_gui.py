from tkinter import *
from tkinter import messagebox
import onetime

class App:
    def __init__(self, master):
        self.default_alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,?!@\/|;'#:~[]{}_+-=()*&^%$<>"

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
        self.alphabet_text.insert(END, self.default_alphabet)
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
        plain = self.plain.get(1.0, END).rstrip('\n')
        key = self.key.get(1.0, END).rstrip('\n')
        self.cypher.delete(1.0, END)
        codec = onetime.codec()
        cypher = codec.encrypt(plain, key, self.alphabet)
        self.cypher.insert(END, cypher)

    def do_decrypt(self):
        self.populate_alphabet()
        cypher = self.cypher.get(1.0, END).rstrip('\n')
        key = self.key.get(1.0, END).rstrip('\n')
        self.plain.delete(1.0, END)
        codec = onetime.codec()
        plain = codec.decrypt(cypher, key, self.alphabet)
        self.plain.insert(END, plain)

    def show_error(self, title, message):
        messagebox.showinfo(title, message)

    def populate_alphabet(self):
        self.alphabet = list(self.alphabet_text.get(1.0, END))

root = Tk()
root.wm_title("Onetime")
app = App(root)
root.mainloop()
