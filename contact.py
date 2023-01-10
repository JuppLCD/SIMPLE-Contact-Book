class Contact:
    def __init__(self, name: str, email: str, phone: str) -> None:
        self.__name = name
        self.__email = email
        self.__phone = phone

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def phone(self):
        return self.__phone

    def update(self, email: str, phone: str):
        self.__email = email
        self.__phone = phone

    def __str__(self) -> str:
        return f'{self.name},{self.email},{self.phone}'

    def show(self):
        print('*'*10)
        print(f'Name: {self.name}')
        print(f'Email: {self.email}')
        print(f'Phone: {self.phone}')
        print('*'*10)
