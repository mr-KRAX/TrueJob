
"""
Модуль задающий и реализующий модели 
для общения DBManager-а и REST_API

Для удобства использования объект каждого класса
можно преобразовать в словарь(dict) и обратно (см. __main__)
"""

from dataclasses import dataclass, asdict


@dataclass
class User:
  """
  Класс Пользователь
  """

  _vkid:             str   # vkid
  _type:             str   # Admin, Regular
  _employer_rating:  float  # 0.0 - 5.0
  _worker_rating:    float  # 0.0 - 5.0
  _status:           str   # Silver, Gold, Platinum
  _is_blocked:       int   # 0, 1

  _possible_type = ("Admin", "Regular")
  _possible_status = ("Silver", "Gold", "Platinum")

  @staticmethod
  def check_type_value(type):
    if not (type in User._possible_type):
      return False
    return True

  @staticmethod
  def check_rating_value(rating):
    if (rating > 5.0 or rating < 0):
      return False
    return True

  @staticmethod
  def check_status_value(status):
    if not (status in User._possible_status):
      return False
    return True

  @staticmethod
  def check_is_blocked_value(is_blocked):
    if not (is_blocked in (0, 1)):
      return False
    return True

  @property
  def vkid(self):
    return self._vkid

  @vkid.setter
  def vkid(self, value):
    self._vkid = str(value)

  @property
  def type(self):
    return self._type

  @type.setter
  def type(self, value):
    if not User.check_type_value(value):
      raise ValueError("Invalid type value",  value)
    self._type = value

  @property
  def employer_rating(self):
    return self._employer_rating

  @employer_rating.setter
  def employer_rating(self, value):
    if not User.check_rating_value(value):
      raise ValueError("Invalid employer_rating value",  value)
    self._employer_rating = value

  @property
  def worker_rating(self):
    return self._worker_rating

  @worker_rating.setter
  def worker_rating(self, value):
    if not User.check_rating_value(value):
      raise ValueError("Invalid worker_rating value", value)
    self._worker_rating = value

  @property
  def status(self):
    return self._status

  @status.setter
  def status(self, value):
    if not User.check_status_value(value):
      raise ValueError("Invalid status value", value)
    self._status = value

  @property
  def is_blocked(self):
    return self._is_blocked

  @is_blocked.setter
  def is_blocked(self, value):
    if not User.check_is_blocked_value(value):
      raise ValueError("Invalid is_blocked value", value)
    self._is_blocked = value

  def setAttr(self, field_name, value):
    print("Attr name: " + field_name, " Value: ", value)
    setattr(self, field_name, value)

  def asDict(self):
    user_as_dict = dict()
    for k, v in asdict(self).items():
      user_as_dict[k[1:]] = v
    return user_as_dict

  def __init__(self, vkid, type, employer_rating=0.0, worker_rating=0.0, status="Silver",  is_blocked=0):
    self.vkid = vkid
    self.type = type
    self.employer_rating = employer_rating
    self.worker_rating = worker_rating
    self.status = status
    self.is_blocked = is_blocked


"""
Class User
"""


@dataclass
class Offer:
  """
  Класс предложение
  """

  _offer_id:      int
  _name:          str
  _description:   str
  _price:         int  # 100$ 30c == 10030
  _exp_date:      str
  _location:      str
  _status:        str  # Active, InProgress, Hidden, Closed
  _owner:         str  # vkid
  _priority:      str  # Top, Regular, Low
  _time_created:  str
  _views_counter: int
  _likes_counter: int

  _possible_status = ("Active", "InProgress", "Hidden", "Closed")
  _possible_priority = ("Top", "Regular", "Low")

  @staticmethod
  def check_status_value(type):
    if not (type in Offer._possible_status):
      return False
    return True

  @staticmethod
  def check_priority_value(type):
    if not (type in Offer._possible_priority):
      return False
    return True

  @property
  def offer_id(self):
    return self._offer_id

  @offer_id.setter
  def offer_id(self, value):
    self._offer_id = value

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, value):
    self._name = value

  @property
  def description(self):
    return self._description

  @description.setter
  def description(self, value):
    self._description = value

  @property
  def price(self):
    return self._price

  @price.setter
  def price(self, value):
    self._price = value

  @property
  def exp_date(self):
    return self._exp_date

  @exp_date.setter
  def exp_date(self, value):
    self._exp_date = value

  @property
  def location(self):
    return self._location

  @location.setter
  def location(self, value):
    self._location = value

  @property
  def status(self):
    return self._status

  @status.setter
  def status(self, value):
    if (Offer.check_status_value(value)):
      raise ValueError("Invalid status value", value)
    self._status = value

  @property
  def owner(self):
    return self._owner

  @owner.setter
  def owner(self, value):
    self._owner = value

  @property
  def priority(self):
    return self._priority

  @priority.setter
  def priority(self, value):
    if (Offer.check_priority_value(value)):
      raise ValueError("Invalid priority value", value)
    self._priority = value

  @property
  def time_created(self):
    return self._time_created

  @time_created.setter
  def time_created(self, value):
    self._time_created = value

  @property
  def views_counter(self):
    return self._views_counter

  @views_counter.setter
  def views_counter(self, value):
    self._views_counter = value

  @property
  def likes_counter(self):
    return self._likes_counter

  @likes_counter.setter
  def likes_counter(self, value):
    self._likes_counter = value

  def setAttr(self, field_name, value):
    print("Attr name: " + field_name, " Value: ", value)
    setattr(self, field_name, value)

  def asDict(self):
    user_as_dict = dict()
    for k, v in asdict(self).items():
      user_as_dict[k[1:]] = v
    return user_as_dict

  def __init__(self, offer_id, name="", price=0, description="", exp_date="", location="", status="", owner="", priority="Regular", time_created="", views_counter=0, likes_counter=0):
    self.offer_id = offer_id
    self.name = name
    self.description = description
    self.price = price
    self.exp_date = exp_date
    self.location = location
    self.status = status
    self.owner = owner
    self.priority = priority
    self.time_created = time_created
    self.views_counter = views_counter
    self.likes_counter = likes_counter


@dataclass
class Assessment:
  user: str
  assessed_user: str
  assessment_as_worker: float  # None or 0.0 - 5.0
  assessment_as_employer: float  # None or 0.0 - 5.0

  def __init__(self, dictionary):
      """
      Конструктор через словарь
      """
      for key in dictionary:
          setattr(self, key, dictionary[key])


if __name__ == "__main__":
  dict_to_User = {'vkid': 'id', 'type': 'Admin', 'employer_rating': 0.2,
                  'worker_rating': 1, 'status': 'Silver', 'is_blocked': 1}
  print("dict to User: ", dict_to_User)

  # dict -> User
  User_from_dict = User(**dict_to_User)
  User_from_dict.setAttr("type", "Admin")
  print("User from dict: ", User_from_dict)

  # User -> dict
  dict_from_User = asdict(User_from_dict)
  print("dict from User:", dict_from_User)
