#!/bin/bash

# Запускаем выполнение тестов над базой данных, выводя информацию о состоянии тестов.
python3 -m unittest -v DataBaseManagerTests.py

# После тестов удаляем временную базу данных для тестов
rm truejob_database.db

