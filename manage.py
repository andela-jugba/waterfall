from flask_script import Manager, Shell
from app import create_app
import os

app = create_app(os.environ.get('WATER_CONFIG', 'default'))

manager = Manager(app)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()