# Write a program that finds whether a given post is talking about "Maham" or not
post=input("Enter the post: ")

#making both the post and string to search in lowercase so in every form its detected
#as python is case sensitive
if("Maham".lower() in post.lower()):
    print("Maham is mentioned in post")
else:
    print("Not talking about Maham")