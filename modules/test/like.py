from modules.test.user import User
from modules.test.post import Post

class Like:
    id: int
    user: User
    post: Post

    def __init__(self, id: int, user: User, post: Post):
        self.id = id
        self.user = user
        self.post = post
