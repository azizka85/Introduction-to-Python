from typing import List

from modules.test.like import Like
from modules.test.user import User
from modules.test.post import Post

class LikeRepository:
    __likes: List[Like]

    def __init__(self):
        users = [
            User(1, 'FirstName1', 'LastName1', 'test@1.again'),
            User(2, 'FirstName2', 'LastName2', 'test@2.again'),
            User(3, 'FirstName3', 'LastName3', 'test@3.again')
        ]

        posts = [
            Post(1, users[0], 'Title #1', 'Text #1', 'Abstract #1'),
            Post(2, users[0], 'Title #2', 'Text #2', 'Abstract #2'),
            Post(3, users[1], 'Title #3', 'Text #3', 'Abstract #3'),
            Post(4, users[2], 'Title #4', 'Text #4', 'Abstract #4')
        ]

        self.__likes = [
            Like(1, users[2], posts[1]),
            Like(2, users[1], posts[3]),
            Like(3, users[0], posts[0]),
            Like(4, users[0], posts[2])
        ]

    @property
    def likes(self):
        return self.__likes
