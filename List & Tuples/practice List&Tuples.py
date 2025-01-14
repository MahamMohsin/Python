#ENTER NAMES OF THREE FRUITS GIVEN INPUT BY USER IN A LIST
fruits=[]

f1=input("Enter fruit name: ")
fruits.append(f1)
f2=input("Enter fruit name: ")
fruits.append(f2)
f3=input("Enter fruit name: ")
fruits.append(f3)
print(fruits)

#INPUT MARKS OF 2 STUDENTS AND DISPLAY IN SORTED MANNER
marks=[]
s1=int(input("Enter student1 marks: "))
marks.append(s1)

s2=int(input("Enter Student2 marks: "))
marks.append(s2)

marks.sort()
print(marks)

#SUM A LIST WITH 3 NUMBERS
#marks sum being done jus to test function
print(sum(marks))
