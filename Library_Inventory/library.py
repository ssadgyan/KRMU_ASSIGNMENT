# ============================================
# Library Management System
# Name: Sadgyan Singh
# Assignment 3
# ============================================

import json
from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.load_data()

    # ---------------------------- BOOK MANAGEMENT ----------------------------
    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))
        self.save_data()

    # ---------------------------- MEMBER MANAGEMENT --------------------------
    def register_member(self, name, member_id):
        self.members.append(Member(name, member_id))
        self.save_data()

    # ---------------------------- BORROW A BOOK ------------------------------
    def lend_book(self, member_id, isbn):
        member = self.get_member(member_id)
        book = self.get_book(isbn)

        if member and book:
            if member.borrow_book(book):
                print(f"{member.name} successfully borrowed '{book.title}'")
                self.save_data()
            else:
                print("Book is not available.")
        else:
            print("Invalid member or book.")

    # ---------------------------- RETURN A BOOK ------------------------------
    def take_return(self, member_id, isbn):
        member = self.get_member(member_id)
        book = self.get_book(isbn)

        if member and book:
            if member.return_book(book):
                print(f"Book '{book.title}' returned successfully.")
                self.save_data()
            else:
                print("This book was not borrowed by the member.")
        else:
            print("Invalid details.")

    # ---------------------------- HELPERS -----------------------------------
    def get_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def get_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    # ---------------------------- DATA PERSISTENCE ---------------------------
    def save_data(self):
        try:
            with open("books.json", "w") as f:
                json.dump([b.to_dict() for b in self.books], f, indent=4)

            with open("members.json", "w") as f:
                json.dump([m.to_dict() for m in self.members], f, indent=4)

        except Exception as e:
            print("Error saving data:", e)

    def load_data(self):
        try:
            with open("books.json", "r") as f:
                self.books = [Book.from_dict(b) for b in json.load(f)]

            with open("members.json", "r") as f:
                self.members = [Member.from_dict(m) for m in json.load(f)]

        except:
            # No file exists initially
            self.books = []
            self.members = []

    # ---------------------------- ANALYTICS ----------------------------------
    def library_report(self):
        borrowed_count = sum(not b.available for b in self.books)
        print("\n===== Library Report =====")
        print(f"Total Books: {len(self.books)}")
        print(f"Borrowed Books: {borrowed_count}")
        print(f"Active Members: {len(self.members)}")
        print("===========================\n")
