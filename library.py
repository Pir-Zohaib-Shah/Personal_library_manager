import json  

def library():
    
    try:
        with open('library.txt', 'r') as f:
            books = json.load(f)
    except FileNotFoundError:
        books = []

    while True:
        print("\nWelcome to the library")
        print("\n1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            print("\nAdding a new book")
            print("Enter the book details:")
            title = input("\nTitle: ").strip()
            author = input("Author: ").strip()
            
            # Year validation
            while True:
                year = input("Year: ").strip()
                if year.isdigit():
                    year = int(year)
                    break
                else:
                    print("Invalid year. Please enter a valid number.")
            
            genre = input("Genre: ").strip()
            
            # Read status validation
            while True:
                read = input("Read (yes/no): ").strip().lower()
                if read == 'yes':
                    read = True
                    break
                elif read == 'no':
                    read = False
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            new_book = {
                'title': title,
                'author': author,
                'year': year,
                'genre': genre,
                'read': read,
            }
            books.append(new_book)
            print(f"\nBook '{title}' added successfully.\n")

        elif choice == '2':
            if not books:
                print("\nNo books in the library to remove.\n")
            else:
                title_to_remove = input("Enter the title of the book to remove: ").strip()
                # Find books with matching title (case-insensitive)
                books_to_remove = [b for b in books if b['title'].lower() == title_to_remove.lower()]
                
                if not books_to_remove:
                    print(f"\nNo books found with title '{title_to_remove}'.\n")
                else:
                    # Remove all matching books (or adjust to handle multiple matches)
                    for book in books_to_remove:
                        books.remove(book)
                    print(f"\nRemoved {len(books_to_remove)} book(s) titled '{title_to_remove}'.\n")

        elif choice == '3':
            if not books:
                print("\nNo books in the library to search.\n")
                continue
                
            print("\nSearch By:")
            print("1. Title")
            print("2. Author")
            search_choice = input("\nEnter your choice: ").strip()

            if search_choice == '1':
                title = input("Enter the title of the book: ").strip()
                found_books = [b for b in books if b['title'].lower() == title.lower()]
                if found_books:
                    print(f"\nFound {len(found_books)} book(s) with the title '{title}':")
                    for idx, b in enumerate(found_books, 1):
                        print(f"{idx}. {b['title']} by {b['author']} ({b['year']}) - {b['genre']} - {'Read' if b['read'] else 'Not Read'}")
                else:
                    print(f"\nNo books found with the title '{title}'.")

            elif search_choice == '2':
                author = input("Enter the author of the book: ").strip()
                found_books = [b for b in books if b['author'].lower() == author.lower()]
                if found_books:
                    print(f"\nFound {len(found_books)} book(s) by '{author}':")
                    for idx, b in enumerate(found_books, 1):
                        print(f"{idx}. {b['title']} by {b['author']} ({b['year']}) - {b['genre']} - {'Read' if b['read'] else 'Not Read'}")
                else:
                    print(f"\nNo books found by '{author}'.")
            else:
                print("\nInvalid choice. Please try again.")

        elif choice == '4':
            if not books:
                print("\nNo books in the library.\n")
            else:
                print("\nAll books in the library:")
                for idx, book in enumerate(books, start=1):
                    print(f"\n{idx}. '{book['title']}' by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Not Read'}")

        elif choice == '5':
            if not books:
                print("\nNo books in the library to display statistics.\n")
            else:
                total_books = len(books)
                read_books = sum(1 for b in books if b['read'])
                print(f"\nTotal books: {total_books}")
                print(f"Percentage of books read: {read_books / total_books * 100:.2f}%")

        elif choice == '6':
            # Save books to file before exiting
            with open('library.txt', 'w') as f:
                json.dump(books, f)
            print("\nLibrary data saved. Exiting the library.")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1-6.")

library()