# A spam comment is defined as a text containng:
# "Make alot of money","buy now","subscribe this","click this"
# Write a program to detect these spams

#USAGE OF IN KEYWORD 
#substring checker in string basically
#for instance if p1 in message will return True

p1="Make alot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

message=input("Enter your comment: ")
if((p1 in message)or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is spam!")
else:
    print("Not spam!")
