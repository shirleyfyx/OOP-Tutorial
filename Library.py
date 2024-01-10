# encapsulate book details
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

        def get_info(self):
            return f"{self.title} by {self.author}, ISBN: {self.isbn}"

class Person:
    def __init__(self, name):
        self.name = name

# inherit from the Person class
class Librarian(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def display(self):
        return f"Librarian: {self.name}, ID: {self.employee_id}"

class Member(Person):
    def __init__(self, name, member_id):
        super().__init__(name)
        self.member_id = member_id
        self.borrowed_books = []

    def display(self):
        borrowed_titles = [book.title for book in self.borrowed_books]
        return f"Member: {self.name}, ID: {self.member_id}, Books: {borrowed_titles}"

# Use abstraction to manage books and members
class Library:
    def __init__(self):
        self.book = []
        self.members = []
    
    def add_book(self, book):
        self.book.append(book)
    
    def add_member(self, member):
        self.members.append(member)
    
    def find_book(self, title):
        for book in self.book:
            if book.title == book:
                return book
        return None
    
    def checkout_book(self, title, member_id):
        book = self.find_book(title)
        if book: 
            member = next((m for m in self.members if m.member_id == member_id), None)
            if member:
                member.borrowed_books.append(book)
                self.book.remove(book)
                return f"{title} has been checked out to {member_id}."
            else:
                return "Member not found."
        return "Book not found."
    
# Creating books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "123456789")
book2 = Book("1984", "George Orwell", "987654321")

# Creating members
member1 = Member("Alice", "M001")
member2 = Member("Bob", "M002")

# Creating a library and adding books and members
my_library = Library()
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_member(member1)
my_library.add_member(member2)

# Checking out a book
print(my_library.checkout_book("The Great Gatsby", "M001"))

# Displaying member details
print(member1.display())