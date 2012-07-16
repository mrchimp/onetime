import os
import onetime_inc

response = "hello"

#letters_list = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",".",",","?","!","@"]
#letters_dict = {' ':0,'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'i':15,'o':16,'p':17,'q':18,'r':19,'s':20,'t':21,'u':22,'v':23,'w':24,'x':25,'y':26,'z':27,'.':28,',':29,'?':30,'!':31,'@':32}

def show_letters():
    for x in range(len(letters_list)):
        print(str(x) + ": " + letters_list[x])

def f_encrypt():
    filename = input("Please input URL: ")
    

def menu():
    response = input("1: Encypt, 2: Decrypt, 3: Encrypt File, 4: Decrypt File, Q: Quit")
    if response == "1":
        inputString = input("Input your plaintext: ")
        c_encrypt(inputString)
        menu()
    elif response == "2":
        inputString = input("Input your cypher: ")
        c_decrypt(cypher)
        menu()
    elif response == "3":
        fileString = input("Input URL of file to encrypt: ")
        if os.path.isfile(fileString):
            plainfile = open(fileString, "r").read()
            cryptfile = onetime.encrypt(plainfile)
            targetfile = open(fileString, "w")
            targetfile.write(cryptfile)
            targetfile.close()
        print("File encrypted successfully")
        menu()
    elif response == "4":
        fileString = input("Input URL of file to decrypt: ")
        if os.path.isfile(fileString):
            cryptfile = open(fileString, "r").read()
            plainfile = onetime.decrypt(cryptfile)
            targetfile = open(fileString, "w")
            targetfile.write(plainfile)
            targetfile.close()
        print("File decrypted successfully!")
        menu()

menu()
