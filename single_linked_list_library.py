class Book:
    def __init__(self, title):
        self.title = title
        self.next = None

class Visitor:
    def __init__(self, name):
        self.name = name
        self.books = None

    def borrow_book(self, title):
        new_book = Book(title)
        
        if self.books is None:
            self.books = new_book
        else:
            current = self.books
            while current.next is not None:
                current = current.next
            current.next = new_book

        print("Buku '{}' telah dipinjam oleh {}.".format(title, self.name))

    def print_borrowed_books(self):
        if self.books is None:
            print("{} belum meminjam buku apapun.".format(self.name))
        else:
            print("Daftar buku yang dipinjam oleh {}:".format(self.name))
            current = self.books
            while current is not None:
                print("- {}".format(current.title))
                current = current.next

visitor1 = Visitor("Upii")
visitor2 = Visitor("Paii")

visitor1.borrow_book("The Overcoat, Nikolai Gogol")
visitor1.borrow_book("Crime and Punishment, Fyodor Dostoevsky")

visitor2.borrow_book("No Longer Human, Osamu Dazai")

visitor1.print_borrowed_books()
visitor2.print_borrowed_books()
