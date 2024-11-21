
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False 

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = [] 

    def add_book(self, book):
        self.books.append(book)
        print(f"{book} has been added to the library.")

    def show_books(self):
        if not self.books:
            print("The library has no books.")
        else:
            print(f"Books in {self.name}:")
            for book in self.books:
                status = "Available" if not book.is_borrowed else "Borrowed"
                print(f"- {book} ({status})")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_borrowed:
                book.is_borrowed = True
                print(f"You've borrowed {book}. Enjoy reading!")
                return
        print("Sorry, this book is either unavailable or already borrowed.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_borrowed:
                book.is_borrowed = False
                print(f"Thank you for returning {book}.")
                return
        print("This book wasn't borrowed from this library.")


def main():
    
    my_library = Library("Community Library")


    my_library.add_book(Book("The legendary mechanic", "chocolion"))
    my_library.add_book(Book("1984", "George Orwell"))
    my_library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))

    
    while True:
        print("\nLibrary Menu:")
        print("1. Show Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            my_library.show_books()
        elif choice == "2":
            book_title = input("Enter the title of the book to borrow: ")
            my_library.borrow_book(book_title)
        elif choice == "3":
            book_title = input("Enter the title of the book to return: ")
            my_library.return_book(book_title)
        elif choice == "4":
            print("Thank you for using the Library System!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
