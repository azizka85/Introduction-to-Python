class Person():
    name: str
    email: str

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def greet(self) -> str:
        return f'Hello {self.name}!'
    
    def check_email(self, email: str) -> bool:
        return self.email == email
    

