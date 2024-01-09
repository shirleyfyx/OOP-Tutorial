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
