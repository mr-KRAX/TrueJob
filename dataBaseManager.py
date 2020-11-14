"""
Модуль общения с базой данных, непосредственно 
направляющий и обрабатывающий запросы к бд

TODO:
  !!! Написать все запросы
  !!! Разработать и реализовать интерфейс модуля
"""
import sqlite3
from sqlite3 import Error
import dataBaseReqs as dbr

### ---------------------------- CREATE DATABASE ----------------------------

def DB_createDatabase():
    try: 
        db = sqlite3.connect('users.db')
        return db
    except Error:
        print(Error)
        return 0

### ---------------------------- CREATING TABLES ----------------------------

def DB_createUsersTable(db):
    cursor = db.cursor()
    cursor.execute(dbr.create_users_table)
    db.commit()

def DB_createOffersTable(db):
    cursor = db.cursor()
    cursor.execute(dbr.create_offers_table)
    db.commit()

def DB_createLikedOffersTable(db):
    cursor = db.cursor()
    cursor.execute(dbr.create_liked_offers)
    db.commit()

def DB_createAssessmentsTable(db):
    cursor = db.cursor()
    cursor.execute(dbr.create_assessments)
    db.commit()

def DB_createReportsTable(db):
    cursor = db.cursor()
    cursor.execute(dbr.create_reports)
    db.commit()

### ---------------------------- START DATABASR ----------------------------

def DB_startDatabase():
    database = DB_createDatabase()
    DB_createUsersTable(database)
    DB_createOffersTable(database)
    DB_createLikedOffersTable(database)
    DB_createReportsTable(database)
    DB_createAssessmentsTable(database)
    return database

def DB_addUser(db):
  cursor = db.cursor()
  cursor.execute("SELECT vkid FROM users")
  if cursor.fetchone() is None:
    cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)",
                   ('Dmitrii', ''))

def add_user_to_table(db):
    cursor = db.cursor()
    cursor.execute("SELECT vkID FROM users")
    if cursor.fetchone() is None:
      cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)",
                     ('John', 1, 4.7, 2.1, 'CoolGuy', 'Typical'))
      db.commit()