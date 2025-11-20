# ============================================
# Main Menu
# Name: Sadgyan Singh
# Assignment 3
# ============================================

from library import Library

def main():
    print("\n===== Welcome to Library Inventory System =====\n")
    lib = Library()

    while True:
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Library Report")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            title = input("Book Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            lib.add_book(title, author, isbn)

        elif choice == "2":
            name = input("Member Name: ")
            member_id = input("Member ID: ")
            lib.register_member(name, member_id)

        elif choice == "3":
            member_id = input("Member ID: ")
            isbn = input("ISBN: ")
            lib.lend_book(member_id, isbn)

        elif choice == "4":
            member_id = input("Member ID: ")
            isbn = input("ISBN: ")
            lib.take_return(member_id, isbn)

        elif choice == "5":
            lib.library_report()

        elif choice == "6":
            print("\nThank you for using Library System!")
            break

        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
