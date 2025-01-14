#PRINT CONTENT OF A LIST USING WHILE LOOP
list=[1,"Maham",True,"CS",3,"F"]

#length is 7
i=0
while(i<len(list)):
    print(list[i])
    i+=1


print("\nSTEP SIZE IN FOR LOOP:")    
#USING FOR LOOP WITH STEP SIZE
for i in range(0,50,4):
    print(i)#skips gap of 4
    
    
print("\nPRINTING LIST USING FORLOOP")
#printing above list elements using for loop
for i in (list):
    print(i)

    
#SAME FORMAT FOR TUPLE
t=(23,"Work Hard",24)
print("\nTUPLE FOR LOOP: ")
for i in (t):
    print(i)
    

#STRINGS
print("\nStrings using for loop:")
s="Maham"
for i in (s):
    print(i)

#USING WHILE LOOP
print("\nStrings using while loop:")    
j=0
while(j<len(s)):
    print(s[j])
    j+=1
    

#FOR LOOP WITH ELSE
print("\nFOR LOOP WITH ELSE STATEMENT")
l=["Good things","take","time"]

for item in (l):
    print(item)    
else:
    print("Well said!")#printed when for loop exhausted
 
#BREAK STATEMENT IN LOOPS
#used to come out of a loop when a certain condition met
print("\nBREAK STATEMENT USAGE: ")
for i in range(10):
    if(i==3):#i==3 reached simply goes out of loop
        print("i==3 condition reached!")
        break
    print(i)   


#CONTINUE STATEMENT IN LOOPS IS USED TO SKIP A ITERATION
#means in above case output: 0 1 2 4 5...9
print("\nCONTINUE STATEMENT USAGE: ")
for i in range(10):
    if(i==3):#i==3 reached simply goes out of loop
        print("i==3 condition reached!")
        continue
    print(i)  
 
   
#PASS KEYWORD SKIPS A CERTAIN CODE ALLOWING YOU TO RUN THE CODE WRITTEN BELOW WITHOUT ERROR
print("\nPASS KEYWORD USAGE: ")
for i in range(18):
    pass

for i in range(5):
    print(i)