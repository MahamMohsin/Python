#Write a program that tells whether a student has passed or failed if it requires a total of 40% and atleast 33% in each course to pass
#Take input for 3 subjects from user

marks1=int(input("Enter marks 1: "))
marks2=int(input("Enter marks 2: "))
marks3=int(input("Enter marks 3: "))

total=marks1+marks2+marks3
percentage=(total/300)*100

if(percentage>=40):
    if(marks1>=33 and marks2>=33 and marks3>=33):
        print("YOU HAVE PASSED!")
        print("Your percentage is: ",percentage,"%")
else:
    print("YOU HAVE FAILED!")
