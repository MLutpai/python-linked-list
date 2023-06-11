class Item:
    def __init__(self, name, importance):
        self.name = name
        self.importance = importance
        self.next = None

class Backpack:
    def __init__(self):
        self.head = None

    def add_item(self, name, importance):
        new_item = Item(name, importance)

        # Jika tas masih kosong, tambahkan item sebagai head
        if self.head is None:
            self.head = new_item
        else:
            # Temukan posisi yang tepat untuk memasukkan item berdasarkan tingkat kepentingan
            if importance > self.head.importance:
                new_item.next = self.head
                self.head = new_item
            else:
                current = self.head
                while current.next is not None and importance <= current.next.importance:
                    current = current.next

                new_item.next = current.next
                current.next = new_item

        print("Item '{}' dengan tingkat kepentingan {} telah ditambahkan ke dalam tas.".format(name, importance))

    def remove_item(self, name):
        if self.head is None:
            print("Tas kosong.")
            return

        if self.head.name == name:
            self.head = self.head.next
            print("Item '{}' telah dihapus dari tas.".format(name))
            return

        current = self.head
        prev = None

        while current is not None:
            if current.name == name:
                prev.next = current.next
                print("Item '{}' telah dihapus dari tas.".format(name))
                return

            prev = current
            current = current.next

        print("Item '{}' tidak ditemukan dalam tas.".format(name))

    def print_items(self):
        if self.head is None:
            print("Tas kosong.")
            return

        current = self.head
        print("Daftar Item dalam Tas:")
        while current is not None:
            print("- Item: {}, Tingkat Kepentingan: {}".format(current.name, current.importance))
            current = current.next

# Contoh penggunaan
backpack = Backpack()

# Menambahkan item ke dalam tas
backpack.add_item("Pedang", 5)
backpack.add_item("Potion", 3)
backpack.add_item("Perisai", 2)

# Mencetak daftar item dalam tas
backpack.print_items()

# Menghapus item dari tas
backpack.remove_item("Potion")

# Mencetak daftar item dalam tas setelah penghapusan
backpack.print_items()
