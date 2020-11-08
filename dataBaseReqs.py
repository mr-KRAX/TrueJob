"""
Вспомогательный модуль где перечислены все запросы к БД
И описаны модели и таблицы
"""




"""
TABLE-1 users

PK user_id: vkid
type: Admin, Regular
employer_rating: 0.0 - 5.0
worker_rating: 0.0 - 5.0
status: Silver, Gold, Platinum
is_blocked: 0, 1
"""
create_users_table = """CREATE TABLE IF NOT EXISTS users(
user_id INT PRIMARY KEY,
type TEXT,
employer_rating REAL,
worker_rating REAL,
status TEXT,
is_blocked INT);
"""


"""
TABLE-2 offers

PK offer_id:
name:
discription:
price:
exp_date:
location:
offer_id:
status: Active, InProgress, Hidden, Closed
owner: vkid
priority: Top, REg, Low
time_created:
views_counter
likes_counter
"""
create_offers_table = """CREATE TABLE IF NOT EXISTS offers(
offer_id INT PRIMARY KEY,
name TEXT,
discription TEXT,
price INT,
exp_date TEXT,
location TEXT,
status TEXT,
owner INT,
priority TEXT,
time_created TEXT,
views_counter INT,
likes_counter INT
"""

"""
TABLE-3 LikedOffers (Связь пользователь - понравившееся предложение)

PK user: vkid
PK offer_id: 
"""

"""
TABLE-4 Assessments (Связь Пользователь - Оцененный пользователь)

PK user: vkid
PK role: worker, employer
PK assessed_user: vkid
assessment: 0.0 - 5.0  #Крайняя оценка
date: 
"""

"""
TABLE-5 Reports (Связь Пользователь - непристойное объявление)

PK user: vkid
PK offer_id: 
"""




