def myFunc():
    print("Hello maham!")

if __name__ == "__main__":#we only want to run it here
    print("We are directly running this")    
    myFunc()
    print(__name__)#if i run this on main i get to see its file name i.e module there and here where i run it

myFunc() #will run on main