# ============================================
# Book Class
# Name: Sadgyan Singh
# Assignment 3 - Library Inventory System
# Date: 20 Nov 2025
# ============================================

class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def borrow(self):
        """Marks book as not available"""
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        """Marks book as available"""
        self.available = True

    def to_dict(self):
        """Convert book object to dictionary (for JSON saving)"""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available
        }

    @staticmethod
    def from_dict(data):
        return Book(
            data["title"],
            data["author"],
            data["isbn"],
            data["available"]
        )
