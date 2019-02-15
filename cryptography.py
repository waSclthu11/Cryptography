"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
strlist=([associations[w:w+1] for w in range(0, 26, 1)]) # Converts to list
text="test"
key="hi"
textlist=[]
x=0 
while x<len(text):
    y=associations.find(text[x])
    textlist.append(y)
    x=x+1
print (textlist)