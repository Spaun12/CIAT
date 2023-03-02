#Week4 Assignment Part1 Michael Connell

class Book:
    def __init__(self, title, author, publisher):
        # Constructor method, initializes the data attributes
        self._title = title
        self._author = author
        self._publisher = publisher

    def get_title(self):
        # Accessor method for the title attribute
        return self._title

    def set_title(self, title):
        # Mutator method for the title attribute
        self._title = title

    def get_author(self):
        # Accessor method for the author attribute
        return self._author

    def set_author(self, author):
        # Mutator method for the author attribute
        self._author = author

    def get_publisher(self):
        # Accessor method for the publisher attribute
        return self._publisher

    def set_publisher(self, publisher):
        # Mutator method for the publisher attribute
        self._publisher = publisher

    def __str__(self):
        # Special method that returns a string representation of the object
        # Formatted with the title, author, and publisher attributes
        return f"Title: {self._title}\nAuthor: {self._author}\nPublisher: {self._publisher}"

# Example usage of the Book class
my_book = Book("The Great Gatsby", "F. Scott Fitzgerald", "Scribner")
print(my_book)

my_book.set_author("Francis Scott Fitzgerald")
print(my_book)