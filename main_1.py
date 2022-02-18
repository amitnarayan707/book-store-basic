from http.client import EXPECTATION_FAILED, SWITCHING_PROTOCOLS
import sqlite3
import os

def get_book(title):
    library = sqlite3.connect('library.db')
    book = library.cursor()
    sql = "SELECT * FROM library WHERE title='{}'".format(title)
    book.execute(sql)
    try:
         return book.fetchone()
    except:
        return "Not found"
def set_book(quantities,title,author,price):
    """ It is use for insert new book in database
set_book(quantities,title,author,price)"""
    library = sqlite3.connect('library.db')
    book = library.cursor()
    try:
        book.execute("""
        CREATE TABLE library(
        quantities INTGER,
        title TEXT,
        author TEXT,
        price INTGER
        );""")
        book.execute("INSERT INTO library (quantities,title,author,price) VALUES(?,?,?,?)",(quantities,title,author,price))
    except:
          book.execute("INSERT INTO library (quantities,title,author,price) VALUES(?,?,?,?)",(quantities,title,author,price))
    library.commit()
    library.close()
    return "Book added"

print("""What do you want to do
1. Search Book
2. Add new book detail
""")
option = int(input("Enter the option no.:"))
while option!=1 and option!= 2:
    print("Worng Input:")
    option = int(input("Enter the option no:"))

if option == 1:
    TOTAL_COST = 0
    NXT='y'
    while NXT == 'y':
        BOOK_NAME = input("Book Title: ")
        book = get_book(BOOK_NAME)
        print(book)
        COPIES = int(input("\nNo. of copies: "))
        TOTAL_COST+=book.price * COPIES.price
        NXT = input("Add more books?Y/N: ")
        NXT = NXT.lower()
    else: print("Total Cost: {}".format(TOTAL_COST))
elif option ==2:
    quant = int(input("Enter quantities of book: "))
    title = input("Enter name of book: ")
    author = input("Enter author name: ")
    price = int(input("Enter price of book: "))
    p = set_book(quant,title,author,price)
    print(p)

