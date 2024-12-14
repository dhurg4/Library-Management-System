import json
import os

#Using a json file to store my library 
filepath = "/Users/dhurgadharani/Desktop/Southampton/P&C/Library management system/library.json"
library =  {} 

#Allowing the program to read the json file, and storing it into a variable called 'library'
with open(filepath, 'r') as f:
    library = json.load(f)

#The function that allows the user to add books into the library.
def add (title, author, ISBN, genre, pubyear, status):
    booknum = ISBN
    #The user would have entered all the necessary inputs, so it will be recorded and added intot he library.
    book =  ["ID", booknum, "Title", title, "Author ", author, "ISBN ", ISBN, "Genre ", genre, "Publication Year ", pubyear, "Status", "AVAILABLE"]
    library[booknum] = book
    print("Here is the added book: ")
    print(library[booknum])
    #It is also printed so the user may check if they've made any mistakes, and may choose to edit it next.
    
def edit (title, author, ISBN, genre, pubyear, status):
    booknum = ISBN
    if booknum in library:
        print (library[booknum])
        cont = input("Is this the book you want to edit?(Y/N): ")
        cont = cont.upper()
        if cont == "Y":
            #This makes sure that only the things that were inputted are changes.
            #If they input 0 into that category, nothing will be changed.
            #The ISBN and Status cannot be changed here.
            if title!= "0":
                library[booknum] =  ["ID", library[booknum][1], "Title", title, "Author ", library[booknum][5], "ISBN ", library[booknum][7], "Genre ", library[booknum][9], "Publication Year ", library[booknum][11], "Status", library[booknum][13]]
            if author != "0":
                library[booknum] =  ["ID", library[booknum][1], "Title", library[booknum][3], "Author ", author, "ISBN ", library[booknum][7], "Genre ", library[booknum][9], "Publication Year ", library[booknum][11], "Status", library[booknum][13]]
            if genre != "0":
                library[booknum] =  ["ID", library[booknum][1], "Title", library[booknum][3], "Author ", library[booknum][5], "ISBN ", library[booknum][7], "Genre ", genre, "Publication Year ", library[booknum][11], "Status", library[booknum][13]]
            if pubyear != "0":
                library[booknum] =  ["ID", library[booknum][1], "Title", library[booknum][3], "Author ", library[booknum][5], "ISBN ", library[booknum][7], "Genre ", library[booknum][9], "Publication Year ", pubyear, "Status", library[booknum][13]]
            print(library[booknum])
        else:
            print("The ISBN for the book you entered does not exist in this library.")
            #To edit ISBN, they have to delete the book and re-enter everything by adding the book again.
            #This is because the ISBN is the primary key.

    
def delete (title, author, ISBN, genre, pubyear, status):
    booknum = ISBN
    #The user must know the ISBN of the book to delete it.
    if booknum in library:
        print(library[booknum])
        cont = input("Are you sure you want to delete this book?(Y/N): ")
        cont = cont.upper()
        if cont == "Y":
            del library[booknum]
            print ("The book has been deleted. ")
    else:
        print("The ISBN for the book you entered does not exist in this library.")
    

def find (title, author, ISBN, genre, pubyear, status):
    list1 = []
    #It will search the json file for anything that matches anything the user entered.
    #Then it will add the books titles and ISBN that matches what the user has entered, and return it.
    #This is in case the user doesn't know all the information about the book.
    for keys, values in library.items():
        if values[1] == ISBN or values[3] == title or values[5] == author or values[9] == genre or values[11] == pubyear:
            list1.append(values[1:14:2])
    print(list1)

def borrow(title, author, ISBN, genre, pubyear, status):
    booknum = ISBN
    #The user must know the ISBN to borrow a book.
    #This will change the status of the book to 'on loan' so if a user searches for it, it will show that it is on loan.
    if booknum in library:
        print (library[booknum])
        cont = input("Is this the book you want to check out?(Y/N): ")
        cont = cont.upper()
        if cont == "Y":
            library[booknum] =  ["ID", library[booknum][1], "Title", library[booknum][3], "Author ", library[booknum][5], "ISBN ", library[booknum][7], "Genre ", library[booknum][9], "Publication Year ", library[booknum][11], "Status", "ON LOAN"]
            print (library[booknum])
        else:
            print("Going back to entryscreen.")

    else:
        print("The ISBN for the book you entered does not exist in this library.")

def returning(title, author, ISBN, genre, pubyear, status):
    booknum = ISBN
    #The user must know the ISBN to return a book.
    #This will change the status of the book to 'available' so if a user searches it up, it will show that it is available. 
    if booknum in library:
        print (library[booknum])
        cont = input("Is this the book you want to return?(Y/N): ")
        cont = cont.upper()
        if cont == "Y":
            library[booknum] =  ["ID", library[booknum][1], "Title", library[booknum][3], "Author ", library[booknum][5], "ISBN ", library[booknum][7], "Genre ", library[booknum][9], "Publication Year ", library[booknum][11], "Status", "AVAILABLE"]
            print (library[booknum])
    else:
        print("The ISBN for the book you entered does not exist in this library.")
    
def inputs():
    #This function is used for every single function as all of them require the user to enter information on the book.
    #To avoid redundancy, I've put all of it into one subroutine, that can be called each time.
    booktitle = input ("Enter the TITLE of the book: ")
    booktitle = booktitle.upper()
    bookauthor = input ("Enter the AUTHOR of the book: ")
    bookauthor = bookauthor.upper()
    bookISBN = input ("Enter the ISBN of the book: ")
    bookgenre = input ("Enter the GENRE of the book: ")
    bookgenre = bookgenre.upper()
    bookpubyear = input ("Enter the PUBLICATION YEAR of the book: ")
    bookstatus = input("Enter the STATUS of the book: ")
    bookstatus = bookstatus.upper()
    return booktitle, bookauthor, bookISBN, bookgenre, bookpubyear, bookstatus;

def entryscreen():
    print ("Hello. Welcome to My Library Management System.")
    print (" - A to ADD  a book into the system.")
    print (" - E to EDIT  a book in the system.")
    print (" - D to DELETE a book in the system.")
    print (" - F to FIND a book in the system.")
    print (" - B to BORROW/CHECK OUT a book in the system.")
    print (" - R to RETURN a book in the system.")
    print (" - N to EXIT THE SYSTEM.")
    user = input("Enter the LETTER of the task you wish to perform: ")
    return user

validinput = False

#The while loop ensures the program will keep running until the user decides to exit from the program.
while validinput == False:
    task = entryscreen()
    task = task.upper()

    if (task == "A"):
        proceed = input("You want to ADD a book. Proceed? Y/N: ")
        proceed = proceed.upper()
        if (proceed == "Y"):
            add (*inputs())
            #The '*' will put all of the variables returned from inputs into the function being called. 

    
    elif (task == "E"):
        proceed = input("You want to EDIT a book. Proceed? Y/N: ")
        proceed = proceed.upper()
        if (proceed == "Y"):
            print("You MUST enter the ISBN of the book. ")
            print ("Enter 0 into the categories you don't want to change. ")
            edit (*inputs())
    
    elif (task == "D"):
        proceed = input("You want to DELETE a book. Proceed? Y/N: ")
        proceed = proceed.upper()
        if (proceed == "Y"):
            print ("You MUST enter the ISBN.")
            delete (*inputs())

    
    elif (task == "F"):
        proceed = input("You want to FIND a book. Proceed? Y/N: ")
        proceed = proceed.upper()
        if (proceed == "Y"):
            print ("Enter 0 into the categories you don't know.")
            find (*inputs())
            
    elif (task == "B"):
        proceed = input("You want to BORROW a book. Proceed? Y/N: ")
        proceed = proceed.upper()
        if (proceed == "Y"):
            print ("You MUST enter the ISBN.")
            borrow(*inputs())

    elif (task == "R"):
        proceed = input("You want to RETURN a book. Proceed? Y/N: ")
        proceed = proceed.upper()
        if (proceed == "Y"):
            print ("You MUST enter the ISBN.")
            returning(*inputs())
            
    elif (task == "N"):
        validinput = True

    else:
        validinput = False
        print ("Invalid input.")

#This is calling all the functions for each thing the user can do with the system.

with open (filepath, 'w') as f:
    json.dump(library, f, indent = 4)
#This dumps all the information changed back into the json file so everything is saved for the next time the program is used. 
