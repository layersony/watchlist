import unittest
from app.models import Movie, User


class MovieTest(unittest.TestCase):
  def setUp(self):
    self.new_movie = Movie(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

  def test_instance(self):
    self.assertTrue(isinstance(self.new_movie, Movie))

class UserModelTest(unittest.TestCase):
  def setUp(self):
    self.new_user = User(password = 'banana')

  def test_password_setter(self):
    self.assertTrue(self.new_user.pass_secure is not None)

  def test_no_access_password(self):
    with self.assertRaises(AttributeError):
      self.new_user.password

  def test_password_verfication(self):
    self.assertTrue(self.new_user.verify_password('banana'))
