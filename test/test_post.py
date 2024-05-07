import os
import sys

sys.path.append(os.getcwd())

import unittest
from modules.test.like_repository import LikeRepository

class TestPost(unittest.TestCase):
    def test_author(self):
        like_repository = LikeRepository()        

        for like in like_repository.likes:
            self.assertIsNotNone(like.post.author)
            self.assertIsNotNone(like.post.author.id)
            self.assertIsNot(like.post.author.id, 0)

if __name__ == '__main__':
    unittest.main()
