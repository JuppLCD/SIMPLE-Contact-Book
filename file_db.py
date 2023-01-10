from contact import Contact


class DBFile:
    def __init__(self, file_name: str, contact_book: list):
        self.file_name = file_name

        self.load_contacts(contact_book)

    def load_contacts(self, contact_book: list) -> None:
        try:
            with open(self.file_name, 'r') as db_file:
                for line in db_file:
                    name, email, phone = line.strip().split(',')
                    contact = Contact(name, email, phone)
                    contact_book.append(contact)
        except FileNotFoundError:
            with open(self.file_name, 'w') as db_file:
                pass

    def refreshing_contacts(self, contact_book: list) -> None:
        with open(self.file_name, 'w') as db_file:
            pass
        with open(self.file_name, 'a') as db_file:
            for contact in contact_book:
                db_file.write(f'{contact}\n')

    def add_contact(self, contact: Contact):
        with open(self.file_name, 'a') as db_file:
            db_file.write(f'{contact}\n')
