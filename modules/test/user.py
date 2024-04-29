class User:
    id: int
    first_name: str
    last_name: str
    email: str

    def __init__(self, id: int, first_name: str, last_name: str, email: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
