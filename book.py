from library import *
import json

class Book:
    
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        Library.bookList.append(self)
    
    def to_dict(self):
        return {
            "Title": self.title,
            "Author": self.author,
            "Year": self.year
        }
    
book1 = Book("Harry Potter", "Samym Mohibby", 2002)
book2 = Book("A song of ice and fire", "Leanne Llena", 2001)
book3 = Book("The Hobbit", "J.R.R. Tolkien", 1937)
book4 = Book("Pride and Prejudice", "Jane Austen", 1813)
book5 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book6 = Book("1984", "George Orwell", 1949)
book7 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book8 = Book("Moby Dick", "Herman Melville", 1851)
book9 = Book("War and Peace", "Leo Tolstoy", 1869)
book10 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
book11 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1954)
book12 = Book("Jane Eyre", "Charlotte Brontë", 1847)
book13 = Book("Crime and Punishment", "Fyodor Dostoevsky", 1866)
book14 = Book("The Odyssey", "Homer", -700)
book15 = Book("Brave New World", "Aldous Huxley", 1932)
book16 = Book("Anna Karenina", "Leo Tolstoy", 1877)
book17 = Book("The Divine Comedy", "Dante Alighieri", 1320)
book18 = Book("Wuthering Heights", "Emily Brontë", 1847)
book19 = Book("Les Misérables", "Victor Hugo", 1862)
book20 = Book("Don Quixote", "Miguel de Cervantes", 1605)
book21 = Book("Fahrenheit 451", "Ray Bradbury", 1953)
book22 = Book("Dracula", "Bram Stoker", 1897)


with open("books.json", "w") as outfile:
    json.dump([book.to_dict() for book in Library.bookList], outfile, indent=2)
