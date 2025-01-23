#CHECKING IF 2 FILES ARE IDENTICAL

with open("filee.txt","r") as f:
    file1=f.read()

with open("filecopy.txt","r") as f:
    file2=f.read()

if (file1==file2):
    print("files are identical")
else:
    print("files are not identical")