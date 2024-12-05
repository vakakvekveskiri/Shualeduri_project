def book_system():
    book_dictionary = {}

    def start_menu():
        print("1. Add a book")
        print("2. Find a book by author")
        print("3. Find a book by title")
        print("4. Exit")

    def add_book(book_dictionary):
        book = input("Enter book name: ")
        if book in book_dictionary:
            print(f"{book} already exists")
        else:
            author = input(f"Enter author for '{book}': ")
            description = input(f"Enter book description for '{book}': ")
            book_dictionary[book] = {"author": author, "description": description}
            print(f"{book} added successfully to dictionary")

    def find_a_book_by_author(book_dictionary):
        author = input("Enter author name: ")
        found_books = [title for title, details in book_dictionary.items() if details['author'] == author]
        if found_books:
            print(f"Books by {author}: {', '.join(found_books)}")
        else:
            print("Author not found")

    def find_a_book_by_title(book_dictionary):
        title = input("Enter book title: ")
        if title in book_dictionary:
            print(f"{title} found: {book_dictionary[title]}")
        else:
            print("Title not found")

    while True:
        start_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_book(book_dictionary)
        elif choice == 2:
            find_a_book_by_author(book_dictionary)
        elif choice == 3:
            find_a_book_by_title(book_dictionary)
        elif choice == 4:
            print("Exiting system.")
            break
        else:
            print("Invalid choice")
