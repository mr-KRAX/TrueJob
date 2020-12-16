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
[+] POST - при регистрации (User user) 
      '{"vkid":str,                 # Обязательный параметр
        "type":"Admin"/"Regular"}'  # Обязательный параметр
      Return:
        Code:
          200/400
        User:
          {
          "vkid": "3",
          "type": "Regular",
          "employer_rating": 0.0,
          "worker_rating": 0.0,
          "status": "Silver",
          "is_blocked": 0
          }
          или
          ["message"]

/user/<vkid>
[+] GET - получить пользователя
      Return:
        Code:
          200/404
        User:
          {
          "vkid": "3",
          "type": "Regular",
          "employer_rating": 0.0,
          "worker_rating": 0.0,
          "status": "Silver",
          "is_blocked": 0
          }
          или
          ["message"]

[+] PUT - изменение состояния пользователя
      Тело запроса:
      '{"type":"Admin"/"Regular",             # Не обязательный параметр
        "status":"Silver"/"Gold"/"Platinum",  # Не обязательный параметр
        "is_blocked":0/1}'                    # Не обязательный параметр
      Return:
        Code:
          200/404/400
        User:
          {
          "vkid": "3",
          "type": "Regular",
          "employer_rating": 0.0,
          "worker_rating": 0.0,
          "status": "Silver",
          "is_blocked": 0
          }
          или
          ["message"]

/user/assess/<vkid>
[-] POST - Поставить пользователю оценку (На стороне api)
        BasicAuth: vkid:*ничего*
        {as_who: “worker/employer”, # Обязательный параметр
         mark: REAL}                # Обязательный параметр

/offers
[+] GET - запросить все объявления

/offers/<str:gps>&<int:radius>
[-] GET - запросить объявления в радиусе (На стороне api)

/offers/owned/<vkid>
[+]  GET - запросить опубликованные объявления по юзеру
/offers/liked/<vkid>
    GET - запрос лайкнутых объявлений по юзеру

/offer/
[+]    POST - опубликовать
      Тело запроса: (Все параметры обязательные)
      '{
        "name":"Offer12", 
        "description":"discription1", 
        "price":100000,               # В копейках(центах и тд)
        "exp_date":"20.10.2020", 
        "location":"Zelenograd", 
        "status":"Active", 
        "owner":"vkid1", 
        "time_created":"12:13 10.10.2020"
        }'
      Return:
        Code:
          200/400
        Offer:
          {
          "offer_id": "gkcpjfzwlw",
          "name": "Offer1",
          "description": "discription1",
          "price": 10,
          "exp_date": "20.10.2020",
          "location": "Zelenograd",
          "status": "Hidden",
          "owner": "vkid1",
          "priority": "Low",
          "time_created": "12:13 10.10.2020",
          "views_counter": 0,
          "likes_counter": 0
          }
          или
          ["message"]
/offer/<int:id>
[+]    GET - получить объявление по id
[+]    PUT - изменить (описание, статус, приорет)
      Тело запроса: (Все параметры НЕ обязательные)
      '{
        "name":"Offer12", 
        "description":"discription1", 
        "price":100000,               # В копейках(центах и тд)
        "exp_date":"20.10.2020", 
        "location":"Zelenograd", 
        "status":"Active", 
        "owner":"vkid1", 
        "time_created":"12:13 10.10.2020"
        }'
      Return:
        Code:
          200/400/404/500
        Измененный Offer:
          {
          "offer_id": "gkcpjfzwlw",
          "name": "Offer1",
          "description": "discription1",
          "price": 10,
          "exp_date": "20.10.2020",
          "location": "Zelenograd",
          "status": "Hidden",
          "owner": "vkid1",
          "priority": "Low",
          "time_created": "12:13 10.10.2020",
          "views_counter": 0,
          "likes_counter": 0
          }
          или
          ["message"]
[+]    DELETE - удалить объявление
      Return:
        Code:
          404/200/500
        Удвленный Offer:
          {
          "offer_id": "gkcpjfzwlw",
          "name": "Offer1",
          "description": "discription1",
          "price": 10,
          "exp_date": "20.10.2020",
          "location": "Zelenograd",
          "status": "Hidden",
          "owner": "vkid1",
          "priority": "Low",
          "time_created": "12:13 10.10.2020",
          "views_counter": 0,
          "likes_counter": 0
          }
          или
          ["message"]
/offer/like/<int:id>
    POST - добавить объявление в избранное
    DELETE - убрать объявление из избранного
/offer/report/<int:id>
    POST(offerId) - пожаловаться
"""

from flask import Flask
from flask_restful import Api, Resource, reqparse, request
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS

import dataBaseManager as DB
import models
# from tools import *

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)
CORS(app)


logOn = False
def logMsg(msg):
  global logOn
  if not (logOn):
    return
  print("LOG: " + str(msg))



@auth.get_password
def get_password(vkid):
  logMsg("vkid authorized: " + vkid)
  return ""
  # for u in users:
  #   print(u.get("vkid"))
  #   if u.get("vkid") == vkid:
  #     print("success")
  #     return "pass"
  # return None

@auth.error_handler
def unauthorized():
    return {'error': 'Unauthorized access'}, 401

class Offers(Resource):
  def get(self, coordinates, radius):
    """
    Запросить объявления в радиусе
    """
    return "Offers", 200


api.add_resource( 
    Offers, "/offers/<string:coordinates>/<int:radius>", endpoint="offers/")
# api.add_resource(Offers, "/offers/", endpoint="offers")

class OffersAll(Resource):
  def get(self):
    """
    Запросить опубликованные объявления
    """
    offers = DB.getAllOffers()
    if offers is None:
      return ["Offers not found"], 404
    return [of.asDict() for of in offers], 200


api.add_resource( 
    OffersAll, "/offers", endpoint="offers")
# api.add_resource(Offers, "/offers/", endpoint="offers")


class OffersOwned(Resource):
  def get(self, vkid):
    """
    Запросить опубликованные объявления по юзеру
    """
    offers = DB.getOffersByUser(vkid)
    if offers is None:
      return ["Offers not found"], 404
    
    return [of.asDict() for of in offers], 200


api.add_resource(OffersOwned, "/offers/owned/<vkid>", endpoint="owned")


class OffersLiked(Resource):
  def get(self, vkid):
    """
    Запросить избранных объявления по юзеру
    """
    return "OffersLiked", 200


api.add_resource(OffersLiked, "/offers/liked/<vkid>", endpoint="liked")


class Offer(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('name', type=str, required=False, location='json')
    self.reqparse.add_argument('description', type=str, required=False, location='json')
    self.reqparse.add_argument('price', type=int, required=False, location='json')
    self.reqparse.add_argument('exp_date', type=str, required=False, location='json')
    self.reqparse.add_argument('location', type=str, required=False, location='json')
    self.reqparse.add_argument('status', type=str, required=False, location='json')
    self.reqparse.add_argument('priority', type=str, required=False, location='json')
    self.reqparse.add_argument('time_created', type=str, required=False, location='json')
 
  def get(self, id):
    """
    Получить объявление по id
    """
    logMsg("GET Offer: " + str(id))
    offer = DB.getOffer(str(id))
    logMsg(offer)
    if offer is None:
      return ["Offer not found"], 404
    return offer.asDict(), 200

  def put(self, id):
    """
    Изменить (описание, статус, приорет)
    """
    offer = DB.getOffer(id)
    if offer is None:
      return ["Offer not found"], 404
    args = dict(self.reqparse.parse_args())
    try:
      for field, value in args.items():
        if value != None:
          offer.setAttr(field, value)
    except ValueError:
      return ["Invalid " + field +" value " + str(value)], 400
    if (DB.updateOffer(offer)):
      return offer.asDict(), 200
    return ["Internal error"], 500

    
  def delete(self, id):
    """
    Удалить пост
    """
    offer = DB.getOffer(id)
    if offer is None:
      return ["Offer not found"], 404
    if(DB.deleteOffer(id)):
      return offer.asDict(), 200
    return ["Internal error"], 500


api.add_resource(Offer, "/offer/<id>", endpoint="offer")


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


class OfferAdd(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('name', type=str, required=True, location='json')
    self.reqparse.add_argument('description', type=str, required=True, location='json')
    self.reqparse.add_argument('price', type=int, required=True, location='json')
    self.reqparse.add_argument('exp_date', type=str, required=True, location='json')
    self.reqparse.add_argument('location', type=str, required=True, location='json')
    self.reqparse.add_argument('status', type=str, required=True, location='json')
    # self.reqparse.add_argument('priority', type=str, required=True, location='json')
    self.reqparse.add_argument('time_created', type=str, required=True, location='json')
    super(OfferAdd, self).__init__()
  
  # @auth.login_required
  def post(self):
    """
    Опубликовать пост
    """
    logMsg("AddUser req:" + str(dict(self.reqparse.parse_args())))
    offerid = models.Offer.get_rand_id()
    while (DB.getOffer(offerid)):
      offerid = models.Offer.get_rand_id()

    try:
      #TODO owner from auth
      offer = models.Offer(offerid, **self.reqparse.parse_args())
    except ValueError as e:
      return e.args, 400
    logMsg("Offer" + str(offer))
    if DB.addOffer(offer):
      return offer.asDict(), 200
    return ["Offer exists"], 400


api.add_resource(OfferAdd, "/offer/")


class OfferReport(Resource):
  def post(self, id):
    """
    Пожаловаться на пост
    """
    return "OfferReport", 200


api.add_resource(OfferReport, "/offer/report/<int:id>", endpoint="report")


class UserAdd(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('vkid', type=str, required=True, location='json')
    self.reqparse.add_argument('type', type=str, required=True, location='json')
    super(UserAdd, self).__init__()

  # @auth.login_required
  def post(self):
    """
    Зарегистрировать нового пользователя
    """
    logMsg("AddUser req:" + str(dict(self.reqparse.parse_args())))
    try:
      user = models.User(**self.reqparse.parse_args())
    except ValueError as e:
      return e.args, 400
    logMsg("User" + str(user))
    if DB.addUser(user):
      return user.asDict(), 200
    return ["User exists"], 400

api.add_resource(UserAdd, "/user/")


class User(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('type', type=str, location='json')
    self.reqparse.add_argument('status', type=str, location='json')
    self.reqparse.add_argument('is_blocked', type=str, location='json')
    super(User, self).__init__()

  # @auth.login_required
  def get(self, vkid):
    """
    Получить пользователя
    """
    logMsg("GET User: " + str(vkid))
    user = DB.getUser(str(vkid))
    logMsg(user)
    if user is None:
      return ["User not found"], 404
    return user.asDict(), 200

  # @auth.login_required
  def put(self, vkid):
    """
    Изменить пользователя
    """
    logMsg("PUT User: "+ str(vkid))
    user = DB.getUser(vkid)
    if user is None:
      return ["User not found"], 404
    args = dict(self.reqparse.parse_args())
    try:
      for field, value in args.items():
        if value != None:
          user.setAttr(field, value)
    except ValueError:
      return ["Invalid " + field +" value " + str(value)], 400
    if (DB.updateUser(user)):
      return user.asDict(), 200
    return ["Internal error"], 500

api.add_resource(User, "/user/<vkid>", endpoint="user")


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


api.add_resource(UserAssess, "/user/assess/<vkid>", endpoint="assess")

if __name__ == '__main__':
    DB.connect()
    DB.initNewConnect()
    app.run(debug=True)
