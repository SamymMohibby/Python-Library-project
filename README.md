# Python-Library-project
This is my first project with which I'll start my python journey. I will add further functionalities to this code and expand it until there isn't anything more to cover. 
This README will at some point contain a table of contents as the project expands further. 

9.9:

Added a json data file to contain all the seperate book objects

FEATURES:
  the program is about a library in which members can register to, borrow books from, and return books to.
  Functions (so far) include things such as borrowing a book, return a book, become a member of the library, Discover a random fun fact or check the overall book catalog.

  The user gets greeted with a menu with all options listed. The user can choose any option at will, although choosing to borrow a book, will lead to the program asking for your member ID, that was initially given to you through a random number+letter generator (given you are a member already.). If you aren't a member, you will have the option to register as a member, granting you full access to the functions. The member data and book items are all saved in a json file, that I will expand further.

Files in the program:
book.py: Class for book objects that has an initializer as well as a format method that makes the books storeable into a seperate json file.

factlist.py: list of random fun facts (Copy-pasted from AI (ChatGPT)) that get selected at random after the user wants a random fact to be printed.

member.py: Class for member items. Initializer only asks for a name and generates a random number+letter combination as an ID for the member.

library.py: Class for a library that has to lists inside it. One for Book objects and the other for Member objects.

functions.py: Pyhton file containing all of the functions neeeded (excluding the main function)

main.py: Main function where the program runs.

members.json: Json file for storing Member objects in a python dictionary format
books.json: Json file for storing Book objects in a python dictionary format.

