# ============================================
# Member Class
# Name: Sadgyan Singh
# Assignment 3 - Library Inventory System
# Date: 20 Nov 2025
# ============================================

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        """Adds a borrowed book"""
        if book.borrow():
            self.borrowed_books.append(book.isbn)
            return True
        return False

    def return_book(self, book):
        """Returns a book"""
        if book.isbn in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book.isbn)
            return True
        return False

    def list_books(self):
        return self.borrowed_books

    def to_dict(self):
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books
        }

    @staticmethod
    def from_dict(data):
        m = Member(data["name"], data["member_id"])
        m.borrowed_books = data["borrowed_books"]
        return m
