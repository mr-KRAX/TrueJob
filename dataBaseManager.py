"""
Модуль общения с базой данных, непосредственно 
направляющий и обрабатывающий запросы к бд

TODO:
  !!! Написать все запросы
  !!! Разработать и реализовать интерфейс модуля
"""
import dataBaseReqs as dbr
import sqlite3

conn = sqlite3.connect('database.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
   vkid INT PRIMARY KEY,
   type TEXT,
   employer_rating REAL,
   worker_rating REAL,
   status TEXT,
   is_blocked
   gender TEXT);
""")