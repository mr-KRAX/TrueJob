
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
  _employer_rating:  float # 0.0 - 5.0
  _worker_rating:    float # 0.0 - 5.0
  _status:           str   # Silver, Gold, Platinum
  _is_blocked:       int   # 0, 1

  _possible_types = ("Admin", "Regular")
  _possible_status = ("Silver", "Gold", "Platinum")

  @staticmethod
  def check_type_value(type):
    if not (type in User._possible_types):
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
    print ("Attr name: " + field_name, " Value: " , value)
    setattr(self, field_name, value)

  def asDict(self):
    user_as_dict = dict()
    for k, v in asdict(self).items():
      user_as_dict[k[1:]] = v
    return user_as_dict


  def __init__(self, vkid, type, employer_rating = 0.0, worker_rating = 0.0, status="Silver",  is_blocked=0):
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

  offer_id:      int
  name:          str
  description:   str
  price:         int  # 100$ 30c == 10030
  exp_date:      str
  location:      str
  status:        str  # Active, InProgress, Hidden, Closed
  owner:         str  # vkid
  priority:      str  # Top, Regular, Low
  time_created:  str
  views_counter: int
  likes_counter: int

  def __init__(self, dictionary):
      """
      Конструктор через словарь
      """
      for key in dictionary:
          setattr(self, key, dictionary[key])


@dataclass
class Assessment:
  user: str
  assessed_user: str
  assessment_as_worker: float # None or 0.0 - 5.0
  assessment_as_employer: float # None or 0.0 - 5.0
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
