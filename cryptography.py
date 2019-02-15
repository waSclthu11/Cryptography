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

#Converting Key to a numbered list
keylist=[]
x=0 
while x<len(key):
    y=associations.find(key[x])
    keylist.append(y)
    x=x+1

#Making the lists equal length
if len(keylist)<len(textlist):
    x=0
    while len(keylist)<len(textlist):
        keylist.append(keylist[x])
        x=x+1
if len(keylist)>len(textlist):
    x=0
    while len(keylist)>len(textlist):
        textlist.append(textlist[x])
        x=x+1
print(keylist)
print(textlist)
#Making Encrypted number list
encryptlist=[]
x=0
while x<len(keylist):
    encryptlist.append(keylist[x]+textlist[x])
    x=x+1
print(encryptlist)
#Making encrypted character list
codelist=[]
x=0
while x<len(encryptlist):
    if encryptlist[x]>84:
        y=encryptlist[x]-84
    else:
        y=encryptlist[x]
    codelist.append(associations[y])
    x=x+1
print(codelist)

