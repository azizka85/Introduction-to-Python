from modules.test.user import User

class Post:
    id: int
    author: User
    title: str
    text: str
    abstract: str

    def __init__(self, id: int, author: User, title: str, text: str, abstract: str):
        self.id = id
        self.author = author
        self.title = title
        self.text = text
        self.abstract = abstract
