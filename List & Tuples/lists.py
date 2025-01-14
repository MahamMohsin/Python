#FOR STORING ELEMENTS WE USE LIST IN PYTHON
friends=["Juice","Apples",False,20]

print(friends[0])
friends[0]=56
print(friends[0])
#unlike strings lists are mutable
#slicing can be can jus like strings
print(friends[0:3])

#here list are being altered but in strings new str is created

#APPEND INSERTS AT END OF LIST
friends.append("Workk")
print(friends)

#SORT sorts the list in ascending
l1=[23,11,44,55]
l1.sort()
print(l1)

friends.reverse()
print(friends)
friends.insert(2,45)#inser 45 at index 2 in list
print(friends)
