#! /usr/bin/python3
from app import create_app, db # from app __init__
# initialize our extension & serve class help us launch out server
from flask_script import Manager, Server
from app.models import User, Role, Review
from flask_migrate import Migrate, MigrateCommand

# create app instance
app = create_app('production')
# app = create_app('test')
migrate = Migrate(app, db) # intialze migrate pass in db and app instance

manager = Manager(app)
manager.add_command('server', Server)
manager.add_command('db',MigrateCommand) #manager command and pass the migratecommand class

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
  return dict(app = app, db = db, User = User, Role = Role, Review=Review)

if __name__ == '__main__':
  manager.run()
