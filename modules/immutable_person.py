class ImmutablePerson():
    __name: str
    __email: str

    def __init__(self, name: str, email: str):
        self.__name = name
        self.__email = email

    def greet(self) -> str:
        return f'Hello {self.__name}!'
    
    def check_email(self, email: str) -> bool:
        return self.__email == email
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def email(self) -> str:
        return self.__email
    
    """ @name.setter
    def name(self, name: str):
        self.__name = name

    @email.setter
    def email(self, email: str):
        self.__email = email """
