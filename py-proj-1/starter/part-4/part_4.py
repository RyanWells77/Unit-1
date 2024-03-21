
books = [{
    "title": "The Eye of the World",
    "author": "Robert Jordan",
    "year": 1990,
    "rating": 5,
    "pages": 782
},
{
    "title": "Warbreaker",
    "author": "Brandon Sanderson",
    "year": 2009,
    "rating": 4.25,
    "pages": 592
},
{
    "title": "The Walking Drum",
    "author": "Louis L'Amour",
    "year": 1984,
    "rating": 3.9,
    "pages": 468
},
{
    "title": "The Book of Three",
    "author": "Lloyd Alexander",
    "year": 1964,
    "rating": 4.25,
    "pages": 217
},
{
    "title": "The Horse and His Boy",
    "author": "C. S. Lewis",
    "year": 1954,
    "rating": 4.25,
    "pages": 199
},
{
    "title": "Ender's Game",
    "author": "Orson Scott card",
    "year": 1985,
    "rating": 4,
    "pages": 324
}]

### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here


def create_new_book():
    
    title = input("What is the title of the book you would like to add?  ")
    author = input("Who is the author of the book you would like to add? ")
    try:
        year = int(input("What year was this book published? "))
    except:
        year = int(input("Please type a number for the year? "))
    try:
        rating = float(input("What rating out of 5 would you give this book? "))
    except:
        rating = float(input("Please type a number between 1 and 5 with up to two decimal places? "))
    try:
        pages = int(input("What is the page count of the book? "))
    except:
        pages = int(input("Please type a number for the number of pages? "))

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    # books.append(book_dictionary)
    return book_dictionary




# print(create_new_book())
# print(type(create_new_book()))
# book = create_new_book()
# for key, value in book.items():
#     print(f"key: {key}, Type: {type(value)}")


### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here





### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here



### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

def search_author (books, author):
    author_match =[]

    for book in books:
        if book["author"].strip().lower() == author.strip().lower():
            author_match.append(book)
    return author_match

def search_title (books, title):
    title_match = []

    for book in books:
        if book["title"].strip().lower() == title.strip().lower():
            title_match.append(book)
    return title_match
    
def library_list (dictionary):
    string = f'{dictionary["title"]}, written by {dictionary["author"]}, was published in {dictionary["year"]}. It has a rating of {dictionary["rating"]} and contains {dictionary["pages"]} pages.'
    return string

def menu (library):

    active = True
    
    while active:
        choice = input("\nMain Menu \nChoose an option below: \nTo look at the library of books press 1. \nTo search for a book by name press 2. \nTo add a new book to the library press 3. \nTo search for book from an author press 4.\nTo exit the menu press 5.")

        if choice == '1':
            for book in library:
                print(library_list(book))
        elif choice == '2':
            search_for_book = input("Enter the title of the book you want to search for: ")
            found_books = search_title(library, search_for_book)
            if found_books:
                print("Book found2:")
                for book in found_books:
                    print(library_list(book))
            else:
                print("Book not found.")
        elif choice == '3':
            new_book = create_new_book()
            if new_book:
                library.append(new_book)
                print("Book added to the library")
            else:
                print("Error adding book. Please try again.")
        elif choice == '4':
            author_name = input("Please enter the name of the author you want to search for: ")
            found_books = search_author(books, author_name)
            if found_books:
                print("Books found by the author:")
                for book in found_books:
                    print(library_list(book))
            else:
                print("No books by that author found.")
        elif choice == '5':
            print('Goodbye')
            active = False

menu(books)
### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

