#Checking the occurance of word python and also print line number
    
with open("Q6text.txt","r") as f:
    #for checking line number
    lines=f.readlines()

lineno=1
occ=0
for line in lines:
    if "Python" in line:
        print("Found at Line number: ",lineno)
        lineno+=1#incrementing line number 
        occ+=1
if occ>0:
        print("Total occurances: ",occ)
else:
    print("No occurance found!")