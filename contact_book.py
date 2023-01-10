import os
from file_db import DBFile
from contact import Contact


class ContactBook:
    def __init__(self, db_file_name: str) -> None:
        self.__contact_book = []
        self.db_file = DBFile(db_file_name, self.__contact_book)

        self.OPTIONS = {
            1: ('Add contact', self.add_contact),
            2:  ('Show all contacts', self.show_all_contacts),
            3: ('Edit contact', self.edit_contact),
            4: ('Delete contact', self.delete_contact),
            5: ('Find contact', self.find_contact),
            0: ('Close',)
        }

    @property
    def contact_book(self) -> list:
        return self.__contact_book

    @contact_book.setter
    def contact_book(self, value: list):
        self.__contact_book = value

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
        continuar = True
        while continuar:
            self.create_section_title(self.OPTIONS[1][0].upper())

            name = input('Name: ')

            in_contact_book = any(self.get_contact_by_name(name))

            if in_contact_book:
                print('There is already a contact with that name')
            else:
                email = input('Email: ')
                phone = input('Phone: ')

                contact = Contact(name, email, phone)
                self.contact_book.append(contact)

                self.db_file.add_contact(contact)
                print('The contact was created successfully')

            more = input('Do you want to add more contacts? (s/n): ')
            if more.lower() != 's':
                continuar = False

    def show_all_contacts(self) -> None:
        self.create_section_title(self.OPTIONS[2][0].upper())

        if (len(self.contact_book) == 0):
            print('There are no contacts.')
        else:
            print(f'There are {len(self.contact_book)} scheduled contacts \n')
            for contact in self.contact_book:
                contact.show()

    def edit_contact(self) -> None:
        self.create_section_title(self.OPTIONS[3][0].upper())

        if (len(self.contact_book) == 0):
            print('There are no contacts.')
        else:
            contact_to_edit = input('Name: ')

            contact = self.get_contact_by_name(contact_to_edit)

            if any(contact):
                contact = contact[0]

                email = input('Email: ')
                phone = input('Phone: ')

                email = contact.email if email.strip() == '' else email
                phone = contact.phone if phone.strip() == '' else phone

                contact.update(email, phone)

                # self.contact_book = list(filter(
                #     lambda contact: contact.name != contact_to_edit, self.contact_book))
                # self.contact_book.append(contact)
                self.db_file.refreshing_contacts(self.contact_book)
                print('Contact successfully edited')
            else:
                print(f'No contacts found with the name: {contact_to_edit}.')

    def delete_contact(self) -> None:
        self.create_section_title(self.OPTIONS[4][0].upper())

        if (len(self.contact_book) == 0):
            print('There are no contacts.')
        else:
            name = input('Name: ')

            contact_to_delete = self.get_contact_by_name(name)

            if any(contact_to_delete):
                contact_to_delete = contact_to_delete[0]

                self.contact_book = list(filter(
                    lambda contact: contact.name != contact_to_delete.name, self.contact_book))
                self.db_file.refreshing_contacts(self.contact_book)

                print('Contact deleted successfully')
            else:
                print(f'No contacts found with the name: {name}.')

    def find_contact(self) -> None:
        self.create_section_title(self.OPTIONS[5][0].upper())

        if (len(self.contact_book) == 0):
            print('There are no contacts.')
        else:
            find_contact = input('Name: ')
            contacts_match = tuple(
                filter(lambda contact: find_contact.lower() in contact.name.lower(), self.contact_book))

            if (len(contacts_match) == 0):
                print(f'No contacts found with the name: {find_contact}.')
            else:
                print(f'There are {len(contacts_match)} scheduled contacts \n')
                for contact in contacts_match:
                    contact.show()

    def get_contact_by_name(self, name: str) -> tuple:
        return tuple(filter(
            lambda contact: contact.name == name, self.contact_book))
