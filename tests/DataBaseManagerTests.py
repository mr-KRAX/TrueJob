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
    self.offer_dict = {"offer_id": 1, "name": "Require a postman", "description": "None",
                 "price": 10030, "exp_date": "today", "location": "everywhere",
                 "status": "Active", "owner": "kdator", "priority": "Top",
                 "time_created": "today", "views_counter": 125, "likes_counter": 34}

  def tearDown(self):
    self.database = DB.closeConnect()

  def test_addUser(self):
    user = User(**self.user_dict)
    self.assertTrue(DB.addUser(user))

  def test_deleteUser(self):
    self.assertTrue(DB.deleteUser("kdator"))

  def test_addOffer(self):
    offer = Offer(self.offer_dict)
    self.assertTrue(DB.addOffer(offer))

  def test_deleteOffer(self):
    self.assertTrue(DB.deleteOffer(1))

if __name__ == '__main__':
  unittest.main()