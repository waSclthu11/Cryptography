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
quit=f
while quit=f:
    enter=input(str(("Enter e to encrypt, d to decrypt, or q to quit: "))
    
    text="test"
    key="hi"
    
    if (enter == "e"):
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
    #Decrypting
    elif enter == "d":
        codelistI=input(str("Message: "))
        key=input(str("Key: "))
        keylist=[]
        x=0 
        while x<len(key):
            y=associations.find(key[x])
            keylist.append(y)
            x=x+1
        
        if len(keylist)<len(codelistI):
            x=0
            while len(keylist)<len(codelistI):
                    keylist.append(keylist[x])
                x=x+1
        
        if len(keylist)>len(codelistI):
            x=0
            while len(keylist)>len(codelistI):
                codelistI.append(codelistI[x])
                x=x+1
        
        codelistII=[]
        x=0 
        while x<len(codelistI):
            y=associations.find(codelistI[x])
            codelistII.append(y)
            x=x+1
        decryptlist=[]
        x=0
        while x<len(codelistI):
            y=codelistII[x]-keylist[x]
            if y<0:
                y=y+84
            else:
                y=y
            decryptlist.append(y)
            x=x+1
        print(decryptlist)
        decryptlistI=[]
        x=0 
        while x<len(decryptlist):
            y=associations[decryptlist[x]]
            decryptlistI.append(y)
            x=x+1
        decryption="".join(decryptlistI)
        print(decryption)
    elif enter=="q":
        quit=t
        print("Goodbye!")
    else:
        print("Did not understand command, try again.")
