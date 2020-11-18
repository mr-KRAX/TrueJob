"""
Модуль общения с базой данных, непосредственно 
направляющий и обрабатывающий запросы к бд

TODO:
  [ ] !!! Написать все запросы
  [+] !!! Разработать и реализовать интерфейс модуля
"""
import dataBaseReqs as dbr
from models import User, Offer, Assessment
import sqlite3


database = None  # Используемая база данных
cursor = None    # Объект взаимодействия с database


"""
DataBaseManager Interface
"""
# Общие функции


def connectToDB():
  """
  Подключиться к базе данных

  return: True, если пожключение успешно, False иначе
  """

  return False


def initNewDB():
  """
  Инициировать новую бд и подключиться к ней

  return: True, если создание и пожключение успешно, False иначе
  """

  return False


# Функции связанные с User
def addUser(user: User):
  """
  Добавить пользователя в бд

  return: True добавление успешно, иначе False 
  """
  return False


def updateUser(user: User):
  """
  Обновить существующего пользователя в бд

  return: True пользователь есть в бд и успешно обновлен, иначе False 
  """
  return False


def getUser(vkid: str):
  """
  Получить пользователя по vkid

  return:  User с id == vkid, иначе None
  """

  return None


def deleteUser(vkid: str):
  """
  Удалить пользователя из бд

  return: True, если успешно, иначе False
  """

  return False


# Функции связанные с Offer
def addOffer(offer: Offer):
  """
  Добавить объявление в бд

  return: True добавление успешно, иначе False 
  """

  return False


def updateOffer(offer: Offer):
  """
  Обновить существующее объявление в бд

  return: True пользователь есть в бд и успешно обновлен, иначе False 
  """

  return False


def getOffer(id: int):
  """
  Получить объявление по id

  return:  User с id == vkid, иначе None
  """

  return None


def deleteOffer(id: int):
  """
  Удалить объявление из бд

  return: True, если успешно, иначе False
  """

  return False


def getOffersByUser(vkid: str):
  """
  Получить объявления опубликованные пользователм с vkid

  return: [Offer, ...] если такие есть, иначе None
  """
  req = "SELECT * FROM Offers WHERE owner=vkid"

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

  return [None]


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
