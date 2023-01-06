import pathlib


def load_contacts_in_db(contact_book: dict, file_name: str) -> None:
    if pathlib.Path(file_name).exists():
        with open(file_name, 'r') as db_file:
            for line in db_file:
                name, email, phone = line.strip().split(',')
                contact_book.setdefault(name, (email, phone))
    else:
        with open(file_name, 'w') as db_file:
            pass


def refreshing_contacts_in_db(contact_book: dict, file_name: str) -> None:
    with open(file_name, 'w') as db_file:
        pass
    with open(file_name, 'a') as db_file:
        for name, data in contact_book.items():
            db_file.write(f'{name},{data[0]},{data[1]}\n')
