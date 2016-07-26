from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app.models import Category, Book
from app import create_app, db
import os

app = create_app(os.environ.get('WATER_CONFIG', 'default'))

manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, Category=Category, Book=Book)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()