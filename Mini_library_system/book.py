import csv

# -----------------------------
# Book Class
# -----------------------------
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, price={self.price!r})"


# -----------------------------
# Library Class
# -----------------------------
class Library:
    def __init__(self, filename="books.csv"):
        self.filename = filename
        self.books = []

    def add_book(self):
        try:
            title = input("Enter Book Title: ").strip()
            author = input("Enter Author Name: ").strip()
            price = float(input("Enter Book Price: "))

            book = Book(title, author, price)
            self.books.append(book)
            print("Book added successfully!")

        except ValueError:
            print("Invalid price! Please enter a number.")

    def display_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\n--- Book List ---")
        for i, book in enumerate(self.books, start=1):
            print(f"{i}. {book.title} | {book.author} | ₹{book.price}")

    def save_to_csv(self):
        try:
            with open(self.filename, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Title", "Author", "Price"])

                for book in self.books:
                    writer.writerow([book.title, book.author, book.price])

            print(f"Books saved to {self.filename}")

        except Exception as e:
            print("Error saving file:", e)

    def load_from_csv(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                header = next(reader, None)  # Skip header if present

                for idx, row in enumerate(reader, start=1):
                    if not row:
                        continue
                    try:
                        title, author, price = row
                        self.books.append(Book(title, author, float(price)))
                    except ValueError:
                        print(f"Skipping malformed row #{idx}: {row}")

            print(f"Books loaded from {self.filename}")

        except FileNotFoundError:
            print("File not found! Please save data first.")
        except Exception as e:
            print("Error reading file:", e)


# -----------------------------
# Main Program
# -----------------------------
def main():
    library = Library()

    while True:
        print("\n---- Library Menu ----")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Save to CSV")
        print("4. Load from CSV")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.display_books()
        elif choice == "3":
            library.save_to_csv()
        elif choice == "4":
            library.load_from_csv()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")


# Run main
if __name__ == "__main__":
    main()
