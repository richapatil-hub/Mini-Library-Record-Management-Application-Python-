import sqlite3

def create_table():
    conn = sqlite3.connect("library.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS books(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    author TEXT,
                    year INTEGER,
                    isbn TEXT,
                    available INTEGER DEFAULT 1
                )''')
    conn.commit()
    conn.close()

def add_book(title, author, year, isbn):
    conn = sqlite3.connect("library.db")
    c = conn.cursor()
    c.execute("INSERT INTO books(title,author,year,isbn,available) VALUES(?,?,?,?,1)",
              (title, author, year, isbn))
    conn.commit()
    conn.close()
    print("Book added!")

def view_books():
    conn = sqlite3.connect("library.db")
    c = conn.cursor()
    c.execute("SELECT * FROM books")
    rows = c.fetchall()
    conn.close()
    for r in rows:
        print(r)

def search_book(keyword):
    conn = sqlite3.connect("library.db")
    c = conn.cursor()
    c.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR isbn LIKE ?",
              ('%'+keyword+'%', '%'+keyword+'%', '%'+keyword+'%'))
    rows = c.fetchall()
    conn.close()
    for r in rows:
        print(r)

def borrow_book(book_id):
    conn = sqlite3.connect("library.db")
    c = conn.cursor()
    c.execute("SELECT available FROM books WHERE id=?", (book_id,))
    row = c.fetchone()
    if row and row[0] == 1:
        c.execute("UPDATE books SET available=0 WHERE id=?", (book_id,))
        print("Book borrowed!")
    else:
        print("Book not available.")
    conn.commit()
    conn.close()

def return_book(book_id):
    conn = sqlite3.connect("library.db")
    c = conn.cursor()
    c.execute("UPDATE books SET available=1 WHERE id=?", (book_id,))
    conn.commit()
    conn.close()
    print("Book returned!")

def delete_book(book_id):
    conn = sqlite3.connect("library.db")
    c = conn.cursor()
    c.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    conn.close()
    print("Book deleted!")

def menu():
    while True:
        print("\n===== Library Menu =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            t = input("Title: ")
            a = input("Author: ")
            y = input("Year: ")
            i = input("ISBN: ")
            add_book(t, a, y, i)
        elif choice == "2":
            view_books()
        elif choice == "3":
            k = input("Search keyword: ")
            search_book(k)
        elif choice == "4":
            b = int(input("Enter Book ID: "))
            borrow_book(b)
        elif choice == "5":
            b = int(input("Enter Book ID: "))
            return_book(b)
        elif choice == "6":
            b = int(input("Enter Book ID: "))
            delete_book(b)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

create_table()
menu()
