import os

letters_list = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",".",",","?","!","@"]

def encrypt(plaintext):
    length = len(plaintext)
    key = fibonnaci(length)
    cypher = ""
    for x in range(length):                         # for each character:
        pnum = find_num(letters_list, plaintext[x]) # plaintext as number
        knum = key[x] % len(letters_list)           # key as number
        cnum = (pnum + knum) % len(letters_list)    # cypher as number
        cletter = letters_list[cnum]                # cypher as letter
        cypher += cletter                           # add char to cypher word
    return cypher

def decrypt(cypher):
    length = len(cypher)
    key = fibonnaci(length)

    plaintext = ""
    for x in range(length):
        cnum = find_num(letters_list, cypher[x])
        knum = key[x] % len(letters_list)
        pnum = (cnum - knum) % len(letters_list)
        pletter = letters_list[pnum]
        plaintext += pletter
    return plaintext

def fibonnaci(limit):
    thearray = []
    a, b = 0, 1
    x = 0
    while x < limit:
        thearray.append(b)
        a, b = b, a+b
        x += 1
    return thearray

def find_num(alphabet, search_str):  #l=list x=search string
  for z in range(len(alphabet)):
    if alphabet[z] == search_str:
      return z


def menu():
    response = input("1: Encypt, 2: Decrypt, 3: Encrypt File, 4: Decrypt File, Q: Quit >>>")
    print(response)
    if response == 1:
        print('test1')
        inputString = input("Input your plaintext: ")
        print('test2')
        print(encrypt(inputString))
        print('test3')
        menu()
    elif response == "2":
        inputString = input("Input your cypher: ")
        print(decrypt(inputString))
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
    else:
        menu()

menu()
