
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

  vkid:             str   # vkid
  type:             str   # Admin, Regular
  employer_rating:  float  # 0.0 - 5.0
  worker_rating:    float  # 0.0 - 5.0
  status:           str   # Silver, Gold, Platinum
  is_blocked:       int   # 0, 1

  def __init__(self, dictionary):
      """
      Конструктор через словарь
      """
      for key in dictionary:
          setattr(self, key, dictionary[key])


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
  dict_to_User = {'vkid': 'id', 'type': 'type', 'employer_rating': 0.2,
            'worker_rating': 0.3, 'status': 'st', 'is_blocked': 1}
  print("dict to User: ", dict_to_User)

  # dict -> User
  User_from_dict = User(dict_to_User)
  print("User from dict: ", User_from_dict)

  # User -> dict
  dict_from_User = asdict(User_from_dict)
  print("dict from User:", dict_from_User)
