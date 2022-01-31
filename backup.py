import os
import shutil

source=input("Enter Source Folder Name")
destination=input("Enter Destination Folder Name")

source=source+'/'
destination=destination+'/'

listoffile1=os.listdir(source)
print(listoffile1)

listoffile2=os.listdir(destination)
print(listoffile2)

for i in listoffile1:
    shutil.move((source+i),destination)

listoffile1=os.listdir(source)
print(listoffile1)

listoffile2=os.listdir(destination)
print(listoffile2)