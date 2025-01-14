#double or single quote is same thng
#an existing string cant be changed

name="maham"
#we can get length of string from length function but if manually
nameshort=name[0:4]  #//means starting from index zero to 2(3 excluded)
charr=nameshort[1]

print(nameshort)#//MAHA printed
print(charr)#//A printed
#0-strlen-1 tk in positive warna in reverse negatives (-1 to on onwards your first letter)
#like for maha a is -1,h is -2,a is -3 and m is -4

#string length
print(len(name))
print(name.endswith("am"))#//should return true
print(name.startswith("ab"))#FALSE

#for capitalizing first letter
print(name.capitalize())

print(name.lower())#CONVERTS TO LOWERCASE ALL
print(name.upper())#UPPERCASE ALL

replaced=name.replace("m","s")
print(replaced)