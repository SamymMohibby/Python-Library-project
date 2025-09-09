from book import *
from library import *
from member import *
from functions import *
import json


def main():
    print(f"List of members:")

    for i in Member.members:
        print(f"{i.memberID}:{i.name}")
    print()
    
    while True:
        choice = menu()
        if choice == 1:
            borrowBook()
        elif choice == 2:
            continue
        elif choice == 3:
            becomeMember()
        elif choice == 4:
            randomFact()
        elif choice == 5:
            checkCatalog()
        elif choice == 0:
            break
        else:
            print("Unknown choice, please select from 1-4 (or 0 to exit).")

    print("Thank you for using the program.")

if __name__ == "__main__":
    main()