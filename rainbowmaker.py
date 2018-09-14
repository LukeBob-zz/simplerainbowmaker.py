## Author Lukebob

import hashlib
import argparse

passlist = []

md5 = "md5"
sha1 = "sha1"
sha224 = "sha224"
sha256 = "sha256"
sha384 = "sha384"
sha512 = "sha512"

parser = argparse.ArgumentParser(description='Create Rainbow Tables With A Supplied Password List.')

parser.add_argument('-p', '--pass_list', help='full path to password list.')
parser.add_argument('-o', '--out_file', help='Name of file to write new rainbow tables to.')
parser.add_argument('-e', '--hash', help='Hash type. Hashes supported [md5, sha1, sha224, sha256, sha384, sha512]')

args = parser.parse_args()

# Usage: (hash, word) = get_hash(md5, "secret word, or itterate wordlist")
def get_hash(hash_type, word):
    global m
    if word != '':
        # Determines hash type
        if hash_type == "md5":
             m = hashlib.md5()
        elif hash_type == "sha1":
             m = hashlib.sha1()
        elif hash_type == "sha224":
             m = hashlib.sha224()
        elif hash_type == "sha256":
             m = hashlib.sha256()
        elif hash_type == "sha384":
             m = hashlib.sha384()
        elif hash_type == "sha512":
             m = hashlib.sha512()

        word1 = word.encode('UTF-8')
        m.update(word1)
        hash =  m.hexdigest()
        return(hash, word)


# Read all entries in password list and add them to passlist
def read_password_list(path_to_wordlist):
    with open(path_to_wordlist, "r") as infile:
        for line in infile:
            if line != "" and line != '\n':
                passlist.append(line[:-1])
    infile.close()


# Writes the word, hash to Defined txt/lst file in {word}:{hash} format
def rainbow_table_append(word, hash, file_name):
    if word and hash != '':

        with open(file_name, "a") as infile:
            infile.write("{0}:{1}\r\n".format(word, hash))
        infile.close()


def main():
    if args.pass_list and args.out_file and args.hash:
        pass_txt = args.pass_list
        out_txt  = args.out_file
        hash     = args.hash
        try:
            read_password_list(pass_txt)
        except:
            print("\n\n[#] Error: Make sure you're providing a full path to the password file.\n\n")
            exit(0)

        try:

            for password in passlist:
                hash, word = get_hash(hash, password)
                rainbow_table_append(word, hash, out_txt)
        except:
            raise

    else:
        parser.print_help()

if __name__ == '__main__':
    main()
