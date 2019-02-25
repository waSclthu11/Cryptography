"""
cryptography.py
Author: waSclthu11
Credit: the previous two challenges
Yikes this is complicated
Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
quit=0
while quit==0:
    enter=input(str(("Enter e to encrypt, d to decrypt, or q to quit: ")))
    
    if enter=="e":
        text=input(str("Message: "))
        key=input(str("Key: "))
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
        
        #Making Encrypted number list
        encryptlist=[]
        x=0
        while x<len(keylist):
            encryptlist.append(keylist[x]+textlist[x])
            x=x+1
        
        #Making encrypted character list
        codelist=[]
        x=0
        while x<len(encryptlist):
            if encryptlist[x]>len(associations):
                y=encryptlist[x]-len(associations)
            else:
                y=encryptlist[x]
            codelist.append(associations[y])
            x=x+1
    
        codelist="".join(codelist)
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
        
        decryptlistI=[]
        x=0 
        while x<len(decryptlist):
            y=associations[decryptlist[x]]
            decryptlistI.append(y)
            x=x+1
        decryption="".join(decryptlistI)
        print(decryption)
    elif enter=="q":
        quit=1
        print("Goodbye!")
    else:
        print("Did not understand command, try again.")
