my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def libary (dictionary):
    string = f'{dictionary["title"]}, written by {dictionary["author"]}, was published in {dictionary["year"]}. It has a rating of {dictionary["rating"]} and contains {dictionary["pages"]} pages.'
    return string

print(libary(my_book))
# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def title (dictionary):
    string = f"Book: {dictionary['title']}"
    return string

def autor (dictionary):
    string =f"Author: {dictionary['author']}"
    return string

def year (dictionary):
    string = f"Published: {dictionary['year']}"
    return string

def rating (dictionary):
    string =f"Rating: {dictionary['rating']}"
    return string

def pages (dictionary):
    string =f"Pages: {dictionary['pages']}"
    return string

print(title(my_book))
print(autor(my_book))
print(year(my_book))
print(pages(my_book))
print(rating(my_book))
# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

