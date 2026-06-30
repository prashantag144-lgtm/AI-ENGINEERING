from pathlib import Path
import os
print("PRESS 1 FOR CREATING A FILE")  
print("PRESS 2 FOR READING A FILE")  
print("PRESS 3 FOR UPDATING A FILE")  
print("PRESS 4 FOR DELETING A FILE") 

check=int(input("PLEASE TELL YOUR RESPONSE"))

def readfileandfolder():
    path=Path('')
    items=list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1}:{items}")

    


def createfile():
    try:    
        readfileandfolder()
        name=input("NAME THIS FILE NAME WHICH YOU WANT TO KEEP IT FOR")
        p=Path(name)
        if not p.exists() and p.is_file:
            with open(p,'w') as fs:
                data=input("what you want to write")
                fs.write(data)

        print("FILE CREATED SUCCESFULLY")
    except Exception as err:
        print(f"AN ERROR OCCURED AT {err}")
    else:
        print("THIS FILE ALREADY EXIST")


        
    
def readfile():
    try:
        readfileandfolder()
        name=input("ENTER WHICH FILE U WANT TO READ")
        p=Path(name)
        if p.exists and p.is_file():
            with open (p,'r') as fs:
                data=fs.read()
                print(data)

            print("FILE READED SUCCESFULLY")
        else:
            print("FILE DOESN'T EXIST")

    except Exception as err:
        print(f" AN ERROR OCCURED IN READING A FILE")


def updatefile():
    try:
        readfileandfolder()
        name=input("ENTER WHICH FILE YOU WANT TO OPEN")
        p=Path(name)
        with open (p,'w') as fs:
            data=input("TYPE WHAT YOU WANT TO UPDATE")
            fs.write(data)

        print("FILE IS UPDATED")

    except Exception as err:
        print(f"THERE IS AN ERROR OCCURED {err}")

""" 
def deletefile():
    try:
        readfileandfolder()
        name=input("ENTER WHICH FILE YOU WANT TO DELETE")
        p=Path(name)
        with open(p,'r') as fs:
            fs.remove(name)
            print("THE FILE IS REMOVED SUCCESFULLY")

    except Exception as err:
        print(f"THIS IS THE EXCEPTION {err}")
 """
def deletefile():
    try:
        readfileandfolder()
        name = input("whuich file you want to delete :- ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(name)
        
            print("file removes suiccessfully ")
    
        else:
            print("No such file exist")
    
    except Exception as err:
        print(f"An error occured as {err}")
if(check==1):
    createfile()
elif(check==2):
    readfile()
elif(check==3):
    updatefile()
elif(check==4):
    deletefile()


