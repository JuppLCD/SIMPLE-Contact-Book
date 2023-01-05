# Contact book
import os

OPTIONS = {
    1: 'Add contact',
    2: 'Show all contacts',
    3: 'Edit contact',
    4: 'Delete contact',
    5: 'Find contact',
    0: 'Close'
}


def create_section_title(title):
    os.system('clear')
    print(f'							{title}')


def show_menu():
    create_section_title('MENU')
    for key, value in OPTIONS.items():
        print(f'{key} ) {value}')


def add_contact(contact_book):
    create_section_title(OPTIONS[1].upper())

    name = input('Name: ')
    email = input('Email: ')
    phone = input('Phone: ')

    contact_book.setdefault(name, (email, phone))

    print('The contact was created successfully')


def show_contacts(contact_book):
    create_section_title(OPTIONS[2].upper())

    if (len(contact_book) == 0):
        print('There are no contacts.')
    else:
        print(f'There are {len(contact_book)} scheduled contacts \n')
        for name, contact in contact_book.items():
            print('*'*10)
            print(f'Name: {name}')
            print(f'Email: {contact[0]}')
            print(f'Phone: {contact[1]}')
            print('*'*10)


def edit_contact(contact_book):
    create_section_title(OPTIONS[3].upper())

    if (len(contact_book) == 0):
        print('There are no contacts.')
    else:
        contact_to_edit = input('Name: ')
        if (contact_book.get(contact_to_edit)):
            email = input('Email: ')
            phone = input('Phone: ')

            contact_book[contact_to_edit] = (email, phone)
            print('Contact successfully edited')
        else:
            print(f'No contacts found with the name: {contact_to_edit}.')


def delete_contact(contact_book):
    create_section_title(OPTIONS[4].upper())

    if (len(contact_book) == 0):
        print('There are no contacts.')
    else:
        contact_to_delete = input('Name: ')
        if (contact_book.get(contact_to_delete)):
            contact_book.pop(contact_to_delete)
            print('Contact deleted successfully')
        else:
            print(f'No contacts found with the name: {contact_to_delete}.')


def find_contact(contact_book):
    create_section_title(OPTIONS[5].upper())

    if (len(contact_book) == 0):
        print('There are no contacts.')
    else:
        find_contact = input('Name: ')
        contacts_match = []
        for name, contact in contact_book.items():
            if (find_contact.lower() in name.lower()):
                contacts_match.append((name, contact))

        if (len(contacts_match) == 0):
            print(f'No contacts found with the name: {find_contact}.')
        else:
            print(f'There are {len(contacts_match)} scheduled contacts \n')
            for name, contact in contacts_match:
                print('*'*10)
                print(f'Name: {name}')
                print(f'Email: {contact[0]}')
                print(f'Phone: {contact[1]}')
                print('*'*10)


def main():
    continuar = True
    contact_book = {}

    while continuar:
        show_menu()
        opt = int(input('Select an option: '))

        if (OPTIONS.get(opt)):
            if (opt == 0):
                continuar = False
                print('Bye, have a nice day')
            elif (opt == 1):
                add_contact(contact_book)
            elif (opt == 2):
                show_contacts(contact_book)
            elif (opt == 3):
                edit_contact(contact_book)
            elif (opt == 4):
                delete_contact(contact_book)
            elif (opt == 5):
                find_contact(contact_book)
        else:
            print('Invalid option')

        if (continuar):
            input('Press to continue...')


if __name__ == '__main__':
    main()
