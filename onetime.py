class codec:

    def encrypt(self, plain, key, alphabet):
        length = len(plain)
        cypher = ""
        for x in range(length):             # for each character:
            pnum = self.find_num(plain[x], alphabet) # plaintext as number
            try:
                knum = self.find_num(key[x], alphabet)   # key as number
            except IndexError:
                self.show_error("Oops", "Key was too short.")
                return 0
            cnum = (pnum + knum) % len(alphabet)    # cypher as number
            cypher += alphabet[cnum]                # cypher as letter
        
        return cypher

    def decrypt(self, cypher, key, alphabet):
        length = len(cypher)
        plain = ""
        for x in range(length):
            cnum = self.find_num(cypher[x], alphabet)
            try:
                knum = self.find_num(key[x], alphabet)
            except IndexError:
                self.show_error("Oops", "Key was too short")
                return 0
            pnum = (cnum - knum) % len(alphabet)
            plain += alphabet[pnum]
        
        return plain
    
    def find_num(self, search_str, alphabet):
        for z in range(len(alphabet)):
            if alphabet[z] == search_str:
                return z

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Encrypt or decrypt a onetime pad.")
    parser.add_argument("action", help="'enc' to encode, 'dec' to decode")
    parser.add_argument("input", help="the cypher or plaintext")
    parser.add_argument("key", help="a random string")
    parser.add_argument("alphabet", help="override the default alphabet", nargs="?")

    args = parser.parse_args()

    default_alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,?!@\/|;'#:~[]{}_+-=()*&^%$<>"

    codec = codec()
    
    if args.alphabet:
        alphabet = args.alphabet
    else:
        alphabet = default_alphabet
    
    if not alphabet:
        import sys
        sys.exit()
    
    if (args.action == 'enc' or args.action == 'encrypt'):
        print codec.encrypt(args.input, args.key, alphabet)
    elif (args.action == 'dec' or args.action == 'decrypt'):
        print codec.decrypt(args.input, args.key, alphabet)
    else:
        print 'What was that?'
