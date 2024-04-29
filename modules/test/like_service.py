from typing import List
from modules.test.like_repository import LikeRepository
from modules.test.user import User

class LikeService:
    like_repository: LikeRepository

    def __init__(self, like_repository: LikeRepository) -> None:
        self.like_repository = like_repository

    @property
    def most_liked_author(self) -> User | None:
        users = {}

        for like in self.like_repository.likes:
            if like.post.author.id in users:
                users[like.post.author.id] = like.post.author, users[like.post.author.id][1] + 1
            else:
                users[like.post.author.id] = like.post.author, 1
        
        max_liked = 0
        max_user: User | None = None

        for k, v in users.items():
            if max_liked < v[1]:
                max_liked = v[1]
                max_user = v[0]
            
        return max_user
