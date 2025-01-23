#volatile in which data doesnt persists(in RAM)
#we can store data in file for it to stay

#2 types of files are: txt file and binary files(incl jpg and all)

#READING A FILE
f=open("file.txt")#as open function is by default read
# print(f.read())
data=f.read()
print(data)
print("Closing file after reading!")
f.close()#closing file

#OVER WRITING IN FILE
# f=open("file.txt","w")#over writes
# f.write("overwritten text")
# f=open("file.txt")
# info=f.read()
# print(info)

#APPENDING IN FILE
f=open("file.txt","a")#over writes
f.write("this is added textt")
f=open("file.txt")
info=f.read()
print(info)

#CREATING A FILE FOR WRITING
# f=open("filee.txt","w")
# st="Maham is a good girl"
# f.write(st)
# f.close()

#READING LINES ONE BY ONE
f=open("filee.txt")
# part1=f.readline()
# print(part1,type(part1))

# part2=f.readline()
# print(part2,type(part2))

# part3=f.readline()
# print(part3,type(part3))

# data=f.readlines()#read all lines
# print(data)

#OR FOR SIMPLY READING ALL LINES
# for line in f:
#     print(line)
#OR
line=f.readline()
while line!="":
    print(line)
    line=f.readline()
f.close()

#FOR NOT EXPLICITELY CLOSING FILE
with open("filee.txt") as f:
    print(f.read())
    
#CREATING COPY FOR A FILE
with open("filee.txt","r") as f:
    content=f.read()
    
with open("filecopy.txt","w") as f:
        f.write(content)
