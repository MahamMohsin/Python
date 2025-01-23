#DO Q4 FOR A LIST OF WORDS TO BE CENSORED

words=["University","BSCS","23K-0594"]
with open("Q5text.txt","r") as f:
    content=f.read()
    
for word in words:
    content=content.replace(word,"#"*len(word))
    
with open("Q5text.txt","w") as f:
    f.write(content) 