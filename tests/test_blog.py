import unittest
from app.models import Blog, User, Comment

class TestPost(unittest.TestCase):
    def setUp(self):
        self.user_Mark = User(first_name = "Sara",
                                last_name = "B",
                                username = "SB",
                                password = "lee",
                                email = "sara@mail.com")
        self.new_post = Blog(blog_title = "One Title",
                            blog_text = "Tired",
                            user_id = self.user_Mark.id)
        self.new_comment = Comment(comment = "Yaay",
                                    blog_id = self.new_blog.id,
                                    user_id = self.user_Sara.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.user_Sara, User))
        self.assertTrue(isinstance(self.new_blog, Blog))
        self.assertTrue(isinstance(self.new_comment, Comment))