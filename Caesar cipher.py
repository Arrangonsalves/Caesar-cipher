def Encryption():
    p=input("Enter Text=")
    ep=''
    for i in p:
        if(i==" "):
            ep=ep+i
            continue
        ep=ep+chr(ord(i)+3)
    print("Cipher Text:",ep)
def Decryption():
    p=input("Cipher Text:")
    ep=''
    for i in p:
        if(i==" "):
            ep=ep+i
            continue
        ep=ep+chr(ord(i)-3)
    print("Original Text:",ep)
if __name__=="__main__":
    p=input("Press E for Encption\nPress D for Decrption\n")
    if(p=="E" or p=="e"):
        Encryption()
    elif(p=="D" or p=="d"):
        Decryption()
    else:
        print("Invalid Input")
        
 
 
 
