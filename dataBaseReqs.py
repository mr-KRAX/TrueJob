"""
Вспомогательный модуль где перечислены все запросы к БД
И описаны модели и таблицы
"""




"""
TABLE-1 users

PK vkid: vkid
type: Admin, Regular
employer_rating: 0.0 - 5.0
worker_rating: 0.0 - 5.0
status: Silver, Gold, Platinum
is_blocked: 0, 1
"""
create_users_table = """CREATE TABLE IF NOT EXISTS users(
vkid TEXT PRIMARY KEY,
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
description:
price:
exp_date:
location:
status: Active, InProgress, Hidden, Closed
owner: vkid
priority: Top, Regular, Low
time_created:
views_counter:
likes_counter:
"""
create_offers_table = """CREATE TABLE IF NOT EXISTS offers(
offer_id INT PRIMARY KEY,
name TEXT,
description TEXT,
price INT,
exp_date TEXT,
location TEXT,
status TEXT,
owner TEXT,
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
PK assessment_role: Worker, Employer
PK assessed_user: vkid
assessment_as_worker: Null или 0.0 - 5.0  #Крайняя оценка
assessment_as_employer: Null или 0.0 - 5.0  #Крайняя оценка
"""

"""
TABLE-5 Reports (Связь Пользователь - непристойное объявление)

PK user: vkid
PK offer_id: 
"""




