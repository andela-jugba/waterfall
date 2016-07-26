import unittest
from flask import current_app
from app import create_app


class BasicAppTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        pass

    def tearDown(self):
        self.app_context.pop
        pass

    def test_app_exits(self):
        self.assertFalse(current_app is None)
        pass

    def test_app_config(self):
        self.assertTrue(current_app.config['TESTING'])

if __name__ == '__main__':
    unittest.main()