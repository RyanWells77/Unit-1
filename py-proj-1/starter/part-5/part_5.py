
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

### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here



def create_new_book():
    
    title = input("What is the title of the book you would like to add?  ")
    author = input("Who is the author of the book you would like to add? ")

    while True:
        try:
            year = int(input("What year was this book published? "))
            if year <= 0:
                year= int(input("Year must be a positive integer."))
            else:
             break
        except:
            year = int(input("Please type a number for the year? "))
    while True:
        try:
            rating = float(input("What rating out of 5 would you give this book? "))
            if not 1 <= rating <= 5:
                rating = float(input("Rating must be a number between 1 and 5"))
            else:
                break
        except:
            rating = float(input("Please type a number between 1 and 5 with up to two decimal places? "))
    while True:
        try:
            pages = int(input("What is the page count of the book? "))
            if pages <= 0:
                pages = int(input("Pages must be a positive number larger than 0"))
            else:
                break
        except:
            pages = int(input("Please type a number for the number of pages? "))

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    with open("library.txt", "a") as f:
        f.write(f"{title}, {author}, {year}, {rating}, {pages}\n")
    return book_dictionary

# create_new_book()

def import_books (books):
     with open("library.txt", "a") as f:
        for book in books:
            f.write(f"{book['title']}, {book['author']}, {book['year']}, {book['rating']}, {book['pages']}\n")

# import_books(books)

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
            
def library_list (dictionary):
    string = f'{dictionary["title"]}, written by {dictionary["author"]}, was published in {dictionary["year"]}. It has a rating of {dictionary["rating"]} and contains {dictionary["pages"]} pages.'
    return string

def print_library_books ():
    with open("library.txt", "r") as f:
        for line in f:
            book_info = line.split(', ')
            book_dictionary = {
                "title": book_info[0],
                "author": book_info[1],
                "year": int(book_info[2]),
                "rating": float(book_info[3]),
                "pages": int(book_info[4])
            }
            print(library_list(book_dictionary))

# print_library_books()
            
### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!
            
def search_title (library, title):
    title_match = []
    with open('library.txt', 'r') as f:
        for line in f:
             book_info = line.strip().split(", ")
             book = {
                "title": book_info[0],
                "author": book_info[1],
                "year": int(book_info[2]),
                "rating": float(book_info[3]),
                "pages": int(book_info[4])
            } 
             if book["title"].strip().lower() == title.strip().lower():
                title_match.append(book)
    return title_match
    
def search_author (library, author):
    author_match =[]

    with open('library.txt', 'r') as f:
        for line in f:
             book_info = line.strip().split(", ")
             book = {
                "title": book_info[0],
                "author": book_info[1],
                "year": int(book_info[2]),
                "rating": float(book_info[3]),
                "pages": int(book_info[4])
            }
             if book["author"].strip().lower() == author.strip().lower():
                author_match.append(book)
    return author_match

def search_years (library, start_year, end_year):
    year_match = []

    with open('library.txt', 'r') as f:
        for line in f:
            book_info = line.strip().split(", ")
            book = {
                "title": book_info[0],
                "author": book_info[1],
                "year": int(book_info[2]),
                "rating": float(book_info[3]),
                "pages": int(book_info[4])
            }
            if start_year <= book["year"] <= end_year:
                year_match.append(book)
    return year_match

def search_rating (library, rating):
    rounded_rating = int(rating)
    rating_match = []

    with open("library.txt", 'r') as f:
        for line in f:
            book_info = line.strip().split(", ")
            book_rating = float(book_info[3])
            if rounded_rating <= book_rating < rounded_rating +1:
                book = {
                    "title": book_info[0],
                    "author": book_info[1],
                    "year": int(book_info[2]),
                    "rating": float(book_info[3]),
                    "pages": int(book_info[4])
                }
                rating_match.append(book)
    return rating_match
            

    

def menu (library):

    active = True
    
    while active:
        choice = input("\nMain Menu \nChoose an option below: \nTo look at the library of books press 1. \nTo search for a book by name press 2. \nTo search for book from an author press 3. \nTo search for any book published in a range of years press 4. \nTo search for books by a rating value press 5. \nTo add a new book to the library press 6. \nTo exit the menu press 7.")

        if choice == '1':
            print_library_books()

        elif choice == '2':
            search_for_book = str(input("Enter the title of the book you want to search for: "))
            if search_for_book.strip().isalpha():
                found_books = search_title("library.txt", search_for_book)
                if found_books:
                    print("Book found2:")
                    for book in found_books:
                        print(library_list(book))
                else:
                    print("Book not found.")
            else:
                print("Book title must contain only alphabetic characters.")

        elif choice == '3':
            author_name = input("Please enter the name of the author you want to search for: ")
            if author_name.strip().isalpha():
                found_books = search_author(books, author_name)
                if found_books:
                    print("Books found by the author:")
                    for book in found_books:
                        print(library_list(book))
                else:
                    print("No books by that author found.")
            else:
                print("Authors name must contain only alphebitic characters.")

        elif choice == '4':
            while True:
                start_year_input = input('Please enter the starting year.')
                end_year_input = input('Please enter the ending year')

                if start_year_input.isdigit() and end_year_input.isdigit():
                    if len(start_year_input) and len(end_year_input) == 4:
                        start_year = int(start_year_input)
                        end_year = int(end_year_input)
                        found_books = search_years(books, start_year, end_year)
                        if found_books:
                            print("Books found to be publised in those years:")    
                            for book in found_books:
                                print(library_list(book))
                        else:
                            print("No books found in thoes years.")
                        break
                    else:
                        print("Please make sure your year is a 4 digit number")
                        break
                else:
                    print("Years must contain only numbers.")
        
        elif choice == '5':
            rating_number = int(float(input("Please input a rating to search for.")))
            found_books = search_rating(books, rating_number)
            if found_books:
                print(f"Books with the rating value of {rating_number}:")
                for book in found_books:
                    print(library_list(book))
            else:
                print(f"No books with the rating of {rating_number} found")
            
        elif choice == '6':
            new_book = create_new_book()
            if new_book:
                print("Book added to the library")
            else:
                print("Error adding book. Please try again.")


        elif choice == '7':
            print('Goodbye')
            active = False

if __name__ == "__main__":
    menu("library.txt")