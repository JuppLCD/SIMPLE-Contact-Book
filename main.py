# Contact book
from contact_book import ContactBook


def main() -> None:
    db_file_name = 'db_contact_book.txt'
    ContactBook(db_file_name).start()


if __name__ == '__main__':
    main()
