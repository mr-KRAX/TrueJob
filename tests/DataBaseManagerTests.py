import unittest

import sys
sys.path.insert(0, '../')

import dataBaseManager as DB
from models import User, Offer, Assessment

class DataBaseManagerTests(unittest.TestCase):

  def setUp(self):
    self.database = DB.connect()
    self.connection = DB.initNewConnect()

    self.user_dict = {"vkid": "kdator", "type": "Admin", "employer_rating": 5.0, 
                 "worker_rating": 4.5, "status": "Gold", "is_blocked": 0}
    self.user_dict_to_upd = {"vkid": "kdator", "type": "Regular", "employer_rating": 4.2, 
                 "worker_rating": 4.1, "status": "Silver", "is_blocked": 0}

  def tearDown(self):
    self.database = DB.closeConnect()

  def test_AddUser(self):
    user = User(**self.user_dict)
    self.assertTrue(DB.addUser(user))

  def test_updateUser(self):
    user = User(**self.user_dict_to_upd)
    self.assertTrue(DB.updateUser(user))

if __name__ == '__main__':
  unittest.main()