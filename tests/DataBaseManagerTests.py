import unittest

import sys
sys.path.insert(0, '../')

import dataBaseManager as DB
from models import User, Offer, Assessment

class DataBaseManagerTests(unittest.TestCase):

  def setUp(self):
    self.database = DB.connect()
    self.connection = DB.initNewConnect()

    self.user_dict_1 = {"vkid": "kdator", "type": "Admin", "employer_rating": 5.0, 
                 "worker_rating": 4.5, "status": "Gold", "is_blocked": 0}
    self.user_dict_2 = {"vkid": "__krax__", "type": "Admin", "employer_rating": 5.0, 
                 "worker_rating": 5.0, "status": "Gold", "is_blocked": 0}
    self.user_dict_to_upd = {"vkid": "kdator", "type": "Regular", "employer_rating": 4.2, 
                 "worker_rating": 4.1, "status": "Silver", "is_blocked": 0}
    self.user_dict_3 = {"vkid": "ni_odnogo_kita", "type": "Regular", "employer_rating": 3.9, 
                 "worker_rating": 5.0, "status": "Silver", "is_blocked": 0}

    self.offer_dict_1 = {"offer_id": 1, "name": "Require a postman", "description": "None",
                 "price": 10030, "exp_date": "24.12.2020", "location": "45.32521", 
                 "status": "Active", "owner": "kdator", "priority": "Top",
                 "time_created": "17.12.2020 12:00", "views_counter": 232, "likes_counter": 123}
    self.offer_dict_2 = {"offer_id": 2, "name": "Require a postman", "description": "None",
                 "price": 25413, "exp_date": "24.12.2020", "location": "45.65431", 
                 "status": "Active", "owner": "kdator", "priority": "Regular",
                 "time_created": "15.12.2020 12:00", "views_counter": 32, "likes_counter": 12}
    self.offer_dict_3 = {"offer_id": 3, "name": "Require a postman", "description": "None",
                 "price": 73923, "exp_date": "24.12.2020", "location": "44.32521", 
                 "status": "Active", "owner": "ni_odnogo_kita", "priority": "Low",
                 "time_created": "17.12.2020 12:00", "views_counter": 232, "likes_counter": 123}

  def tearDown(self):
    self.database = DB.closeConnect()

  def test_01_addUser(self):
    user = User(**self.user_dict_1)
    second_user = User(**self.user_dict_2)
    third_user = User(**self.user_dict_3)
    self.assertTrue(DB.addUser(user))
    self.assertTrue(DB.addUser(second_user))
    self.assertTrue(DB.addUser(third_user))

  def test_01_addOffer(self):
    offer = Offer(**self.offer_dict_1)
    second_offer = Offer(**self.offer_dict_2)
    third_offer = Offer(**self.offer_dict_3)
    self.assertTrue(DB.addOffer(offer))
    self.assertTrue(DB.addOffer(second_offer))
    self.assertTrue(DB.addOffer(third_offer))

  def test_02_updateUser(self):
    user = User(**self.user_dict_to_upd)
    self.assertTrue(DB.updateUser(user))

  def test_03_addOfferLike(self):
    self.assertTrue(DB.addOfferLike("__krax__", 1)) 
    self.assertTrue(DB.addOfferLike("__krax__", 2))
  
  def test_03_getLikedOfferByUser(self):
    krax_liked_offers = list()
    krax_liked_offers.append(Offer(**self.offer_dict_1))
    krax_liked_offers.append(Offer(**self.offer_dict_2))
    self.assertEqual(DB.getLikedOffersByUser("__krax__"), krax_liked_offers)

  def test_04_deleteOffer(self):
    self.assertTrue(DB.deleteOffer(1))

  @unittest.expectedFailure
  def test_05_deleteFakeOffer(self):
    self.assertTrue(DB.deleteOffer(1))

  def test_05_deleteUser(self):
    self.assertTrue(DB.deleteUser("kdator"))

  @unittest.expectedFailure
  def test_05_deleteFakeUser(self):
    self.assertTrue(DB.deleteUser("shokorov_nikita")) 

if __name__ == '__main__':
  unittest.main()