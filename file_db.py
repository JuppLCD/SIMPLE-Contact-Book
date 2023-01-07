class DBFile:
    def __init__(self, file_name: str, contact_book: dir):
        self.file_name = file_name

        self.load_contacts(contact_book)

    def load_contacts(self, contact_book: dir) -> None:
        try:
            with open(self.file_name, 'r') as db_file:
                for line in db_file:
                    name, email, phone = line.strip().split(',')
                    contact_book.setdefault(name, (email, phone))
        except FileNotFoundError:
            with open(self.file_name, 'w') as db_file:
                pass

    def refreshing_contacts(self, contact_book: dict) -> None:
        with open(self.file_name, 'w') as db_file:
            pass
        with open(self.file_name, 'a') as db_file:
            for name, data in contact_book.items():
                db_file.write(f'{name},{data[0]},{data[1]}\n')

    def add_contact(self, contact: tuple):
        with open(self.file_name, 'a') as db_file:
            db_file.write(f'{contact[0]},{contact[1]},{contact[2]}\n')
