from unittest import TestCase
from app.models import Category, Book
from app import db, create_app

class TestModel(TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_catetory_creation(self):
        category_fiction = Category(name='Fiction')
        self.assertEqual(category_fiction.name, 'Fiction')

    def test_classifications(self):
        c1 = Category(name='Hacking')
        c2 = Category(name='Coding')
        book = Book(name='Coding to Hack')
        book.categories.append(c1)
        book.categories.append(c2)
        db.session.add_all([c1,c2,book])
        self.assertEqual(book.categories.count(), 2)
