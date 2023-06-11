class Participant:
    def __init__(self, name, ranking):
        self.name = name
        self.ranking = ranking
        self.next = None

class Tournament:
    def __init__(self):
        self.head = None

    def add_participant(self, name, ranking):
        new_participant = Participant(name, ranking)

        if self.head is None:
            self.head = new_participant
        else:
            if ranking < self.head.ranking:
                new_participant.next = self.head
                self.head = new_participant
            else:
                current = self.head
                while current.next is not None and ranking >= current.next.ranking:
                    current = current.next

                new_participant.next = current.next
                current.next = new_participant

        print("Peserta '{}' dengan peringkat {} telah terdaftar dalam turnamen.".format(name, ranking))

    def remove_participant(self, name):
        if self.head is None:
            print("Daftar peserta kosong.")
            return

        if self.head.name == name:
            self.head = self.head.next
            print("Peserta '{}' telah dihapus dari daftar turnamen.".format(name))
            return

        current = self.head
        prev = None

        while current is not None:
            if current.name == name:
                prev.next = current.next
                print("Peserta '{}' telah dihapus dari daftar turnamen.".format(name))
                return

            prev = current
            current = current.next

        print("Peserta '{}' tidak ditemukan dalam daftar turnamen.".format(name))

    def print_participants(self):
        if self.head is None:
            print("Daftar peserta kosong.")
            return

        current = self.head
        print("Daftar Peserta Turnamen:")
        while current is not None:
            print("- Nama: {}, Peringkat: {}".format(current.name, current.ranking))
            current = current.next


tournament = Tournament()

tournament.add_participant("Beth Harmon", 1)
tournament.add_participant("Benny Watts", 3)
tournament.add_participant("Vasily Borgov", 2)
tournament.add_participant("Harry Beltik", 4)

tournament.print_participants()

tournament.remove_participant("Harry Beltik")

tournament.print_participants()
