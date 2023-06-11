class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.next = None

class TaskList:
    def __init__(self):
        self.head = None

    def add_task(self, description, priority):
        new_task = Task(description, priority)

        if self.head is None:
            self.head = new_task
        else:
            if priority < self.head.priority:
                new_task.next = self.head
                self.head = new_task
            else:
                current = self.head
                while current.next is not None and priority >= current.next.priority:
                    current = current.next

                new_task.next = current.next
                current.next = new_task

        print("Tugas '{}' dengan prioritas {} telah ditambahkan.".format(description, priority))

    def remove_task(self, description):
        if self.head is None:
            print("Daftar tugas kosong.")
            return

        if self.head.description == description:
            self.head = self.head.next
            print("Tugas '{}' telah dihapus.".format(description))
            return

        current = self.head
        prev = None

        while current is not None:
            if current.description == description:
                prev.next = current.next
                print("Tugas '{}' telah dihapus.".format(description))
                return

            prev = current
            current = current.next

        print("Tugas '{}' tidak ditemukan.".format(description))

    def print_tasks(self):
        if self.head is None:
            print("Daftar tugas kosong.")
            return

        current = self.head
        print("Daftar Tugas:")
        while current is not None:
            print("- Tugas: {}, Prioritas: {}".format(current.description, current.priority))
            current = current.next

task_list = TaskList()

task_list.add_task("Membuat Donat Akainu", 2)
task_list.add_task("Menonton Wanpis", 1)
task_list.add_task("Mencari Wanpis", 3)

task_list.print_tasks()

task_list.remove_task("Menonton Wanpis")

task_list.print_tasks()
