import os

class Livros:
    def __init__(self, ):
        self.__lista = [
            
            {"ID": "1",
            "title": "book 1",
            "author": "Leandro",
            "loan": 300.50,
            "return": False},

            {"ID": "2",
            "title": "book 2",
            "author": "Roger",
            "loan": 450.33,
            "return": False}

        ]

    def search(self, book):
        for i in self.__lista:
            if i["title"] == book:
                print(f"Book found: {i}")
                break
    
    def search_author(self, author):
        for i in self.__lista:
            if i["author"] == author:
                print(f"Book found: {i}")
                break

    def list_all_books(self):
        for i in self.__lista:
            print(i['ID'], i['title'], " | ", i['author'], " | ", i['loan'], " | ", i['return'])

    def loan(self, book, price: float):
        if price <= 0:
            print("Invalid value!")
        else:
            for i in self.__lista:
                if i['title'] == book:
                    if price >= i['loan']:
                        print('Book purchased!')
                    else:
                        print('Insufficient money.')
                else:
                    pass
    
    def add_book(self, id: int, title: str, author: str, loan: float, rturn = False):
        book_add = {"ID": id, "title": title, "author": author, "loan": loan, "return": rturn}
        self.__lista.append(book_add)
        print("Book add with success!")

    def return_book(self, book):
        for i in self.__lista:
            if i['title'] == book:
                self.__lista.remove(i)
                return "Book has been returned with success!"
            else:
                return "Book not found"

def clear_term():
    input("\nType any character to continue... ")
    os.system('cls')
            
book = Livros()

while True:
    try:

        print("""Choose one option:

1 - Search by Book
2 - Search by Author
3 - List all books
4 - Buy book
5 - Add book
6 - Return book
7 - Leave
""")

        option_chosen = int(input("Type the number: "))

        if option_chosen < 1 or option_chosen > 7:
            print("Type a valid number!!!\n")
            clear_term()
        else:
            if option_chosen == 1:
                book_searched = input("Write the book you wish to find: ")
                book.search(book_searched)
                clear_term()
            elif option_chosen == 2:
                author_searched = input(" Write the author you wish to find: ")
                book.search_author(author_searched)
                clear_term()
            elif option_chosen == 3:
                book.list_all_books()
                clear_term()
            elif option_chosen == 4:
                book_chosen = str(input("What book you want to buy: "))
                your_value = float(input("\nHow much money do you have: "))
                book.loan(book_chosen, your_value)
                clear_term()
            elif option_chosen == 5:
                id = int(input("Type the book id"))
                title = str(input("\nType the book title: "))
                author = str(input("Type the author of the book: "))
                loan = float(input("Enter the book´s value: "))
                book.add_book(id, title, author, loan)
            elif option_chosen == 6:
                selected_book = str(input("Enter the book´s name: "))
                print(book.return_book(selected_book))
                clear_term()
            else:
                print("Leaving the program...")
                break
    
    except ValueError as e:
        print("Type a number!")