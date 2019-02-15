"""
cryptography.py
Author: waSclthu11
Credit: <list sources used, if any>
Yikes this is complicated
Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
strlist=([associations[w:w+1] for w in range(0, 26, 1)]) # Converts to list
text="test"
key="hi"
#Converting text to a numbered list
textlist=[]
x=0 
while x<len(text):
    y=associations.find(text[x])
    textlist.append(y)
    x=x+1
print(textlist)
#Converting Key to a numbered list
keylist=[]
x=0 
while x<len(key):
    y=associations.find(key[x])
    keylist.append(y)
    x=x+1
print(keylist)
#Attempting to convert to encrypted list
if len(keylist)<len(textlist):
    x=0
    while len(keylist)<len(textlist):
        keylist.append(keylist[x])
        x=x+1
print(keylist)
encryptlist=[]


