# geek term by tuanvc
geek = {"404": "page not found",
        "fap": "masterbate",
        "lol": "laugh out loud"}

def lookup():
    term = input("Term you want to look up: ")
    if term in geek:
        print("Here it is: ", geek[term])
    else:
        while True:
            option = input("Term not found, want to add this new term? y/n?")
            if option == "y":
                addterm(term)
                break
            elif option == "n":
                break
            else:
                print("Invalid option")

def addterm(term):
    definition = input("Definition of the above term: ")
    geek[term] = definition
    print("Term and definition added successful !!!")

def redefine():
    term = input("The term you want to redinife: ")
    if term in geek:
        geek[term] = input("New term is: ")
        print("Redefine done !")
    else:
        print("Sorry, term not found !")

def deleteterm():
    term = input("The term you want to delete: ")
    if term in geek:
        geek.pop(term)
        print("Term deleted successfully !!!")
    else:
        print("Sorry, term not found !")
            
while True:
    choice = int(input("""
This is the dictionary of geek !
0 - Quit
1 - Look up term
2 - Add a new term
3 - Redefine term
4 - Delete term

Your choice: """))
      
    if choice == 0:
        #enter = input("Press enter to exit !")
        break
    elif choice == 1:
        lookup()
    elif choice == 2:
        term = input("The term you want to add: ")
        if term not in geek:
            addterm(term)
        else:
            print("Term already in the dictionary")
    elif choice == 3:
        redefine()
    elif choice == 4:
        deleteterm()
    else:
        print("Invalid option")

    # loop again
    press = input("Press enter to continue")
        
            
                
