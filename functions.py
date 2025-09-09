from member import *
from book import *
from library import *
from list import *

#Menu of the program
def menu():
    print("This is the menu of this program.\nPlease choose one of the following. Press 0 to stop")
    print("1) Borrow a book")
    print("2) Return a book")
    print("3) Become a member of this library")
    print("4) Discover a random fun fact")
    print("5) Check book catalog")
    print("0) Exit the menu")

    choice = int(input("Your choice: "))
    return choice

def randomFact():
    print()
    print(random.choice(random_facts))
    print()
    return None

def becomeMember():
    name = input("Please give us your name: ")
    member = Member(name)

    print(f"Hello {name}, your id is {member.memberID}")

def borrowBook():
    found = False
    memberId = input("Please enter your member ID: ")
    if memberId in Library.memberList:
        bookName = input("Please enter the name of the book you want to borrow: ")
        for book in Library.bookList:
            if bookName == book.title:
                print(f"You have borrowed the book '{book.title}'")
                Library.bookList.remove(book)
                found = True
                print()
                break
        if not found:
            print("We don't have that book...")
            print()
    else:
        print("Sorry you are not a member...")
        print()
    return None

def checkCatalog():
    print()
    for book in Library.bookList:
        print(f"Title: {book.title} | Author: {book.author} | Year published: {book.year}")
    print()
    return None