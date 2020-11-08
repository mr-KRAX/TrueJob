"""
Модуль реализующий REST API для общений клиента с БД
TODO: 
  !!! Реализовать все запросы
  !!! Добавить авторизацию
  !!  Использовать вункции общения с бд из dataBaseManager.py
      Возможно разделить Resource-ы и main в разные модули
"""

"""
REST ЗАПРОСЫ

/user/
    POST - при регистрации
/user/<int:vkid>
    GET - получить пользователя
    PUT - изменение состояния пользователя
/user/assess/<int:vkid>
    POST - Поставить пользователю оценку 
        {as_who: “worker/employer”,
         mark: REAL}

/offers/<str:gps>&<int:radius>
    GET - запросить объявления в радиусе 
/offers/owned/<int:vkid>
    GET - запросить опубликованные объявления по юзеру
/offers/liked/<int:vkid>
    GET - запрос лайкнутых объявлений по юзеру

/offer/<int:id>
    GET - получить объявление по id
    PUT - изменить (описание, статус, приорет)
/offer/like/<int:id>
    POST - добавить объявление в избранное
    DELETE - убрать объявление из избранного
/offer/
    POST - опубликовать
/offer/report/<int:id>
    POST(offerId) - пожаловаться

"""

from flask import Flask
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
api = Api(app)

# NOTE: осторожно хардкод
users = [
    {
        "vkid": 1,
        "type": "Regular",
        "worker_rating": 5.0
    },
    {
        "vkid": 2,
        "type": "Admin",
        "worker_rating": 1.0
    },
    {
        "vkid": 3,
        "type": "Regular",
        "worker_rating": 3.4
    },
    {
        "vkid": 4,
        "type": "Regular",
        "worker_rating": 3.7
    },
]


class Offers(Resource):
  def get(self, coordinates, radius):
    """
    Запросить объявления в радиусе
    """
    return "Offers", 200


api.add_resource( 
    Offers, "/offers/<string:coordinates>/<int:radius>", endpoint="offers")
# api.add_resource(Offers, "/offers/", endpoint="offers")


class OffersOwned(Resource):
  def get(self, vkid):
    """
    Запросить опубликованные объявления по юзеру
    """
    return "OffersOwned", 200


api.add_resource(OffersOwned, "/offers/owned/<int:vkid>", endpoint="owned")


class OffersLiked(Resource):
  def get(self, vkid):
    """
    Запросить избранных объявления по юзеру
    """
    return "OffersLiked", 200


api.add_resource(OffersLiked, "/offers/liked/<int:vkid>", endpoint="liked")


class Offer(Resource):
  def get(self, id):
    """
    Получить объявление по id
    """
    return "Offer get", 200

  def put(self, id):
    """
    Изменить (описание, статус, приорет)
    """
    return "Offer put", 200


api.add_resource(Offer, "/offer/<int:id>", endpoint="offer")


class OfferLike(Resource):
  def post(self, id):
    """
    Добавить объявление в избранное
    """
    return "OfferLike post", 200

  def delete(self, id):
    """
    Убрать объявление из избранного
    """
    return "OfferLike delete", 200


api.add_resource(OffersOwned, "/offer/like/<int:id>", endpoint="like")


class OfferPost(Resource):
  def post(self):
    """
    Опубликовать пост
    """
    return "OfferPost", 200


api.add_resource(OfferPost, "/offer/")


class OfferReport(Resource):
  def post(self, id):
    """
    Пожаловаться на пост
    """
    return "OfferReport", 200


api.add_resource(OfferReport, "/offer/report/<int:id>", endpoint="report")


class UserAdd(Resource):
  def post(self):
    """
    Зарегистрировать нового пользователя
    """
    return "UserAdd", 200


api.add_resource(UserAdd, "/user/")


class User(Resource):
  def get(self, vkid):
    """
    Получить пользователя
    """
    return "User get", 200

  def put(self, vkid):
    """
    Изменить пользователя
    """
    return "User put", 200


api.add_resource(User, "/user/<int:vkid>", endpoint="user")


class UserAssess(Resource):
  def post(self, vkid):
    """
    Поставить оценку пользователю
    NOTE:
    У нас есть 2 вида оцнеки так что надо передать ее тип в теле запроса
    {
      role: “worker/employer”,
      assessed_user
      mark: REAL
    }
    """
    return "UserAssess post", 200


api.add_resource(UserAssess, "/user/assess/<int:vkid>", endpoint="assess")

if __name__ == '__main__':
    app.run(debug=True)
