#DICTIONARY IS A COLLECTION OF KEY AND VALUE PAIR
#FOR EG: STUDENT NAME AND MARKS

marks={
    "Harry":100,
    "Maham":70,
    "Haider":66,
    "list":[34,22,38]
}

print(marks,type(marks))
#print(marks[0]) IS INVALID BUT:
print(marks["Maham"])

#EASY LOOKUP POSSIBLE THRO DICT INSTEAD OF LIST OR LIST OF LIST
print(marks["list"])

#DICTIONARY IS MUTABLE THAT MEANS CHANGABLE
#ITS INDEXED(means if maham searched direct maham pe jakr it will print its value)
#CANT HAVE DUPLICATES

#METHODS

#printing dict keys w/ their values
#print(marks.items())

#printing only keys
print(marks.keys())

#printing only values
print(marks.values())

#updating a key's value(possible bec its mutable)
#marks.update({"Maham":75,"Harry":98,"Sarah":76})
# print(marks)

#Get method used to get value corresponding to the key
print(marks.get("Maham"))
print(marks["Maham"])
#both returns same values but for instance we search for a name that doesnt exist in dict
#then get would return NONE but second method would give ERROR

#SHALLOW COPY OF DICT
newdict=marks.copy()
print(newdict)

#clearing dict
marks.clear()
print(marks)#would display{}

