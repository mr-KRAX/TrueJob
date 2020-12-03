"""
Модуль общения с базой данных, непосредственно 
направляющий и обрабатывающий запросы к бд

TODO:
  [ ] !!! Написать все запросы
  [+] !!! Разработать и реализовать интерфейс модуля
"""
import sqlite3
from sqlite3 import Error

import dataBaseReqs as dbr
from models import User, Offer, Assessment


database = None  # Используемая база данных
cursor = None    # Объект взаимодействия с database


"""
DataBaseManager Interface
"""
# Общие функции


def connect():
  """
  Подключиться к базе данных

  return: True, если подключение успешно, False иначе
  """
  global database
  global cursor
  database = sqlite3.connect('truejob_database.db', check_same_thread=False)
  cursor = database.cursor()
  if database is None or cursor is None:
    return False
  return True

def closeConnect():
  """
  Закрыть соединение с базой данных.
  """
  global database
  database.close()

def initNewConnect():
  """
  Инициировать новую бд и подключиться к ней

  return: True, если создание и подключение успешно, False иначе
  """
  result = connect()
  if result:
    cursor.execute(dbr.create_assessments_table)
    cursor.execute(dbr.create_liked_offers_table)
    cursor.execute(dbr.create_offers_table)
    cursor.execute(dbr.create_reports_table)
    cursor.execute(dbr.create_users_table)
    database.commit()
    return True
  return False


# Функции связанные с User
def addUser(user: User):
  """
  Добавить пользователя в бд

  return: True добавление успешно, иначе False 
  """
  cursor.execute("SELECT vkid FROM users WHERE vkid = (?)", (user.vkid, ))
  if cursor.fetchone() is None:
    cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)",
                   (user.vkid, user.type, user.employer_rating,
                    user.worker_rating, user.status, user.is_blocked))
    database.commit()
    return True
  return False


def updateUser(user: User):
  """
  Обновить существующего пользователя в бд

  return: True пользователь есть в бд и успешно обновлен, иначе False 
  """
  cursor.execute("SELECT vkid FROM users WHERE vkid = (?)", (user.vkid, ))
  if cursor.fetchone() is not None:
    cursor.execute("UPDATE users SET \
        vkid = (?), type = (?), \
        employer_rating = (?), worker_rating = (?), \
        status = (?), is_blocked = (?) \
        WHERE vkid = (?)",
        (user.vkid, user.type, user.employer_rating,
         user.worker_rating, user.status, user.is_blocked,
         user.vkid))
    database.commit()
    return True
  return False


def getUser(vkid: str):
  """
  Получить пользователя по vkid

  return:  User с id == vkid, иначе None
  """
  cursor.execute("SELECT vkid FROM users WHERE vkid = (?)", (user.vkid, ))
  row = cursor.fetchone() # создаём строку из таблицы для удобства проверки 
    # последующей конвертации строки таблицы в словарь.
  if row is not None:
    """
    cursor.description возвращает имена столбцов из последнего запроса.
    он возвращает кортеж из 7 значений, где последние 6 = None.
    на нулевой позиции лежит название столбца, поэтому его и используем для
    формирования словаря.
    """
    rowDict = dict(zip([column[0] for column in cursor.description], row))
    user = User(rowDict)
    return user
  return None


def deleteUser(vkid: str):
  """
  Удалить пользователя из бд

  return: True, если успешно, иначе False
  """
  cursor.execute("SELECT vkid FROM users WHERE vkid = (?)", (vkid, ))
  if cursor.fetchone() is not None:
    cursor.execute("DELETE FROM users WHERE vkid = (?)", (vkid, ))
    database.commit()
    return True
  return False


# Функции связанные с Offer
def addOffer(offer: Offer):
  """
  Добавить объявление в бд

  return: True добавление успешно, иначе False 
  """
  with sqlite3.connect(databaseName) as db:
    cursor = db.cursor()
    cursor.execute("SELECT offer_id FROM offers WHERE offer_id = (?)", (offer.offer_id, ))
    if cursor.fetchone() is None:
      cursor.execute("INSERT INTO offers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
          (offer.offer_id, offer.name, offer.description, offer.price, offer.exp_date,
          offer.location, offer.status, offer.owner, offer.priority, offer.time_created,
          offer.views_counter, offer.likes_counter))
      database.commit()
      return True
    return False


def updateOffer(offer: Offer):
  """
  Обновить существующее объявление в бд

  return: True пользователь есть в бд и успешно обновлен, иначе False 
  """
  with sqlite3.connect(databaseName) as db:
    cursor = db.cursor()
    cursor.execute("SELECT offer_id FROM offers WHERE offet_id = (?)", (offer.offer_id, ))
    if cursor.fetchone() is not None:
      cursor.execute("UPDATE offers SET \
        offer_id = (?), name = (?), \
        description = (?), price = (?), \
        exp_date = (?), location = (?), \
        status = (?), owner = (?), \
        priority = (?), time_created = (?), \
        views_counter = (?), likes_counter = (?) \
        WHERE offer_id = (?)",
        (offer.offer_id, offer.name, offer.description, offer.price, offer.exp_date,
        offer.location, offer.status, offer.owner, offer.priority, offer.time_created,
        offer.views_counter, offer.likes_counter, offer.offer_id))
      database.commit()
      return True
    return False


def getOffer(id: int):
  """
  Получить объявление по id

  return:  Offer с offed_id == id, иначе None
  """
  with sqlite3.connect(databaseName) as db:
    cursor = db.cursor()
    cursor.execute("SELECT * FROM offers WHERE offer_id = (?)", (id, ))
    row = cursor.fetchone() # создаём строку из таблицы объявлений для удобства проверки 
      # и последующей конвертации строки в словарь.
    if row is not None:
      """
      cursor.description возвращает имена столбцов из последнего запроса.
      он возвращает кортеж из 7 значений, где последние 6 = None.
      на нулевой позиции лежит название столбца, поэтому его и используем для
      формирования словаря.
      """
      rowDict = dict(zip([column[0] for column in cursor.description], row))
      offer = Offer(**rowDict)
      return offer
    return None


def deleteOffer(id: int):
  """
  Удалить объявление из бд

  return: True, если успешно, иначе False
  """
  with sqlite3.connect(databaseName) as db:
    cursor = db.cursor()
    cursor.execute("SELECT offer_id FROM offers WHERE offer_id = (?)", (id, ))
    if cursor.fetchone() is not None:
      cursor.execute("DELETE FROM offers WHERE offer_id = (?)", (id, ))
      database.commit()
      return True
    return False


def getOffersByUser(vkid: str):
  """
  Получить объявления опубликованные пользователм с vkid

  return: [Offer, ...] если такие есть, иначе None
  """
  with sqlite3.connect(databaseName) as db:
    cursor = db.cursor()
    cursor.execute("SELECT * FROM offers WHERE owner = (?)", (vkid, ))
    rows = cursor.fetchall()
    if rows is not None:
      list_of_offers = list()
      for row in rows:
        list_of_offers.append(list(row))
      return list_of_offers
    return None


def getLikedOffersByUser(vkid: str):
  """
  Получить лайкнутые пользователем с vkid объявления 
  """
  
  req = "SELECT Offers.* FROM LikedOffers, Offers \
          WHERE LikedOffers.user = vkid \
          AND LikedOffers.offer_id = Offers.offer_id"

  return [None]


def getAllOffers():
  """
  Получить все объявления

  return: [Offer, ...] Все объявления, если есть, иначе None
  """
  with sqlite3.connect(databaseName) as db:
    cursor = db.cursor()
    cursor.execute("SELECT * FROM offers")
    list_of_offers = list(cursor.fetchall())
    if list_of_offers is not None
      return list_of_offers
    return None


# Функции связанные с Like & Report & Assessment
def addOfferLike(vkid: str, offer_id: int):
  """
  Добвить запись о лайке в таблицу TABLE-3 LikedOffers

  return: True, если добавление успешно, иначе False
  """

  return False


def deleteOfferLike(vkid: str, offer_id: int):
  """
  Удалить запись о лайке в таблицу TABLE-3 LikedOffers

  return: True, если запись была и успешно удалена, иначе False
  """

  return False


def addReport(vkid: str, reported_vkid: str):
  """
  Добавить запись о репорте в таблицу TABLE-5 Reports

  return: True, если добавление успешно, иначе False
  """

  return False


def addAssessment(vkid: str, assessed_vkid: str, assessment_as_worker: float = None, assessment_as_employer: float = None):
  """
  Добавить запись об оценке в таблицу TABLE-4 Assessments

  return: True, если добавление успешно, иначе False
  """

  return False


def getAssessment(vkid: str, assessed_vkid: str):
  """
  Получить существующую оценку

  return: Assesment, если такая оценка есть, иначе None
  """

  return None


def updateAsssessment(assessment: Assessment):
  """
  Обновить запись об оценке, если такая есть

  return: True, если такая есть и обновление успешно, иначе False
  """

  return False


def getAllAssessments(assessed_vkid: str):
  """
  Получить все оценки оцененного пользователя

  return: [Assessment, ...] все оценки, если есть, иначе None
  """

  return [None]

# def printResult():
#   cursor = database.cursor()
#   for value in cursor.execute(f"SELECT * FROM users"):
#     print(value)
#   for offer in cursor.execute(f"SELECT * FROM offers"):
#     print(offer)


# if __name__ == "__main__":
#   user_dict_1 = {"vkid": "kdator", "type": "user", "employer_rating": 5.0, 
#             "worker_rating": 4.5, "status": "regular", "is_blocked": 0}
#   user_dict_2 = {"vkid": "kdator", "type": "admin", "employer_rating": 3.3, 
#             "worker_rating": 2.2, "status": "super", "is_blocked": 1}
#   user_dict_3 = {"vkid": "_kr.alex_", "type": "admin", "employer_rating": 5.0,
#             "worker_rating": 5.0, "status": "Gold", "is_blocked": 0}
#   first_offer_json = {"offer_id": 123, "name": "first offer", "description": "stupido",
#                  "price": 10030, "exp_date": "27.01.2021", "location": "Moscow",
#                  "status": "active", "owner": "kdator", "priority": "regular",
#                  "time_created": "26.11.2020", "views_counter": 2, "likes_counter": 3}
#   second_offer_json = {"offer_id": 124, "name": "first offer", "description": "stupido",
#                  "price": 10030, "exp_date": "27.01.2021", "location": "Moscow",
#                  "status": "active", "owner": "kdator", "priority": "regular",
#                  "time_created": "26.11.2020", "views_counter": 2, "likes_counter": 3}
#   first_user = User(user_dict_1)
#   third_user = User(user_dict_3)
#   first_offer = Offer(first_offer_json)
#   second_offer = Offer(second_offer_json)
#   initNewConnect()
#   addUser(first_user)
#   addUser(third_user)
#   addOffer(first_offer)
#   addOffer(second_offer)
#   printResult()
#   print("------------------------")
#   printResult()
#   deleteUser("_kr.alex_")
#   print("------------------------")
#   printResult()
#   list_of_offers = getOffersByUser("kdator")
#   for offer in list_of_offers:
#     print(offer)
#   closeConnect()
