import os
from file_db import DBFile


class ContactBook:
    contact_book = {}

    def __init__(self, db_file_name: str) -> None:
        self.db_file = DBFile(db_file_name, self.contact_book)

        self.OPTIONS = {
            1: ('Add contact', self.add_contact),
            2:  ('Show all contacts', self.show_all_contacts),
            3: ('Edit contact', self.edit_contact),
            4: ('Delete contact', self.delete_contact),
            5: ('Find contact', self.find_contact),
            0: ('Close',)
        }

    def start(self):
        loop = True

        while loop:
            self.show_menu()
            opt = self.select_option()

            if (opt in self.OPTIONS):
                if (opt == 0):
                    loop = False
                    print('Bye, have a nice day')
                else:
                    self.OPTIONS[opt][1]()
            else:
                print('Invalid option')

            if (loop):
                input('Press to continue...')

    def create_section_title(self, title: str) -> None:
        os.system('clear')
        print(f'							{title}')

    def show_menu(self) -> None:
        self.create_section_title('MENU')
        for key, value in self.OPTIONS.items():
            print(f'{key} ) {value[0]}')

    def select_option(self) -> int:
        opt = input('Select an option: ')
        try:
            opt = int(opt)
        except ValueError:
            opt = -1
        return opt

    def add_contact(self) -> None:
        self.create_section_title(self.OPTIONS[1][0].upper())

        name = input('Name: ')

        if self.contact_book.get(name):
            print('There is already a contact with that name')
        else:
            email = input('Email: ')
            phone = input('Phone: ')

            self.contact_book.setdefault(name, (email, phone))
            self.db_file.add_contact((name, email, phone))

            print('The contact was created successfully')

    def show_all_contacts(self) -> None:
        self.create_section_title(self.OPTIONS[2][0].upper())

        if (len(self.contact_book) == 0):
            print('There are no contacts.')
        else:
            print(f'There are {len(self.contact_book)} scheduled contacts \n')
            for name, contact in self.contact_book.items():
                self.show_contact(name, contact[0], contact[1])

    def edit_contact(self) -> None:
        self.create_section_title(self.OPTIONS[3][0].upper())

        if (len(self.contact_book) == 0):
            print('There are no contacts.')
        else:
            contact_to_edit = input('Name: ')
            if (self.contact_book.get(contact_to_edit)):
                email = input('Email: ')
                phone = input('Phone: ')

                self.contact_book[contact_to_edit] = (email, phone)
                self.db_file.refreshing_contacts(self.contact_book)
                print('Contact successfully edited')
            else:
                print(f'No contacts found with the name: {contact_to_edit}.')

    def delete_contact(self) -> None:
        self.create_section_title(self.OPTIONS[4][0].upper())

        if (len(self.contact_book) == 0):
            print('There are no contacts.')
        else:
            contact_to_delete = input('Name: ')
            if (self.contact_book.get(contact_to_delete)):
                self.contact_book.pop(contact_to_delete)
                self.db_file.refreshing_contacts(self.contact_book)
                print('Contact deleted successfully')
            else:
                print(f'No contacts found with the name: {contact_to_delete}.')

    def find_contact(self) -> None:
        self.create_section_title(self.OPTIONS[5][0].upper())

        if (len(self.contact_book) == 0):
            print('There are no contacts.')
        else:
            find_contact = input('Name: ')
            contacts_match = []
            for name, contact in self.contact_book.items():
                if (find_contact.lower() in name.lower()):
                    contacts_match.append((name, contact))

            if (len(contacts_match) == 0):
                print(f'No contacts found with the name: {find_contact}.')
            else:
                print(f'There are {len(contacts_match)} scheduled contacts \n')
                for name, contact in contacts_match:
                    self.show_contact(name, contact[0], contact[1])

    def show_contact(self, name, email: str, phone: str) -> None:
        print('*'*10)
        print(f'Name: {name}')
        print(f'Email: {email}')
        print(f'Phone: {phone}')
        print('*'*10)
