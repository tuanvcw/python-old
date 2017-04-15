# file browser

def readfile():
    location = input("Mode: READ\nenter file location: ")
    file = open(location, "r")
    print("Here's the content of file: \n")
    print(file.read())
    file.close()
    
def updatefile():
    location = input("Mode: UPDATE\/CREATE\nenter file location: ")
    file = open(location, "w")
    content = input("New content: ")
    file.write(content)
    file.close()
    print("Updated !!!")

def addcontent():
    location = input("Mode: APPEND\nenter file location: ")
    file = open(location, "a")
    content = input("New content: ")
    file.write(content)
    file.close()
    print("Appended !!!")

#main
while True:
    print("""
This is the file manager, you can:
0 - Exit the program
1 - View a file
2 - Update content of a file
3 - Append content to a file
""")
    option = int(input("Your option: "))
    if option == 0:
        print("Bye bye")
        break
    elif option == 1:
        readfile()
    elif option == 2:
        updatefile()
    elif option == 3:
        addcontent()
    else:
        print("Invalid option")
        
    enter = input("Hit enter to continue")


