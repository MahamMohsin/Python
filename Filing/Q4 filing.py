#Replace university with school of computing
word="University"
with open("Q4text.txt","r") as f:
    content=f.read()
    
contentNew=content.replace(word,"School of Computing")
    
with open("Q4text.txt","w") as f:
    f.write(contentNew)        