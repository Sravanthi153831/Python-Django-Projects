def add_book():
    book = input("Enter book name: ")

    with open("books.txt", "a") as f:
        f.write(book + "\n")

    print("Book added successfully")


def view_books():
    try:
        with open("books.txt", "r") as f:
            books = f.readlines()

        if not books:
            print("No books found")
        else:
            print("\nLibrary Books:")

            for b in books:
                print("-", b.strip())

    except FileNotFoundError:
        print("No books found")


def search_book():
    try:
        name = input("Enter book to search: ")

        with open("books.txt", "r") as f:
            books = f.readlines()

        found = False

        for b in books:
            if name.lower() in b.lower():
                print("Book found:", b.strip())
                found = True

        if not found:
            print("Book not found")

    except FileNotFoundError:
        print("No books found")


def delete_book():
    try:
        name = input("Enter book to delete: ")

        with open("books.txt", "r") as f:
            books = f.readlines()

        found = False

        with open("books.txt", "w") as f:
            for b in books:
                if name.lower() not in b.lower():
                    f.write(b)
                else:
                    found = True

        if found:
            print("Book deleted")
        else:
            print("Book not found")

    except FileNotFoundError:
        print("No books found")


while True:
    print("\n1.Add 2.View 3.Search 4.Delete 5.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        delete_book()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice")
