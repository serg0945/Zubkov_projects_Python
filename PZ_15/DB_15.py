import sqlite3 as sq
from data import *
import os

if not os.path.exists('wholesale_base.db'):
   with sq.connect('wholesale_base.db') as con:
      con.execute('PRAGMA foreign_keys = ON')  # разрешает работу с внешними ключами
      cur = con.cursor()
      cur.execute("""CREATE TABLE items(
         items_id INTEGER PRIMARY KEY,
         title VARCHAR,
         description VARCHAR,
         unit VARCHAR
      )""")
      cur.execute("""CREATE TABLE markets(
         markets_id INTEGER PRIMARY KEY,
         title VARCHAR,
         address VARCHAR,
         telephone VARCHAR
      )""")
      cur.execute("""CREATE TABLE shop_applications(
         shap_id INTEGER PRIMARY KEY,
         markets_id INTEGER,
         date_application DATE NULL,
         FOREIGN KEY (markets_id) REFERENCES markets(markets_id)
      )""")
      cur.execute("""CREATE TABLE items_num(
         itnum_id INTEGER PRIMARY KEY,
         items_id INTEGER,
         itnum_quantity INTEGER,
         FOREIGN KEY (items_id) REFERENCES items(items_id)
         )""")
      cur.execute("""CREATE TABLE composition(
         com_id INTEGER PRIMARY KEY,
         shap_id INTEGER KEY,
         items_id INTEGER,
         com_quantity INTEGER,
         FOREIGN KEY (shap_id) REFERENCES shop_applications(shap_id),
         FOREIGN KEY (items_id) REFERENCES items(items_id)
         )""")
      cur.executemany("INSERT INTO markets VALUES (?, ?, ?, ?)", markets)
      cur.executemany("INSERT INTO items VALUES (?, ?, ?, ?)", items)
      cur.executemany("INSERT INTO shop_applications VALUES (?, ?, ?)", shop_applications)
      cur.executemany("INSERT INTO items_num VALUES (?, ?, ?)", items_num)
      cur.executemany("INSERT INTO composition VALUES (?, ?, ?, ?)", composition)



with sq.connect('wholesale_base.db') as con:
    cur = con.cursor()
    print('Вывести список всех товаров и описания:\n')
    for result in cur.execute("SELECT title, description FROM items\n"):
      print(result)

    print('\n')
    print('Вывести список всех магазинов и их адресов\n')
    for result in cur.execute("SELECT title, address FROM markets\n"):
       print(result)

    print('\n')
    print('Вывести список всех заявок магазинов и даты, на которые они были поданы\n')
    for result in cur.execute("SELECT markets.title, shop_applications.date_application FROM markets INNER JOIN shop_applications ON markets.markets_id = shop_applications.shap_id\n"):
       print(result)
    
    print('\n')
    print('Вывести список товаров и их количество на складе\n')
    for result in cur.execute("SELECT markets.title, items_num.itnum_quantity FROM markets INNER JOIN items_num ON markets.markets_id = items_num.itnum_id\n"):
       print(result)
    
    print('\n') 
    print('Вывести список товаров и количество их наличия на складе в порядке убывания количества:\n')
    for result in cur.execute("SELECT markets.title, items_num.itnum_quantity FROM markets INNER JOIN items_num ON markets.markets_id = items_num.itnum_id ORDER BY items_num.itnum_quantity DESC\n"):
       print(result)
    
    print('\n')
    print('Вывести список всех заявок магазинов и товаров, которые были в них заказаны:\n')
    for result in cur.execute("SELECT markets.title, items.title FROM markets INNER JOIN items ON markets.markets_id = items.items_id\n"):
       print(result)

    print('\n')
    print('Вывести список всех товаров, у которых на складе количество меньше минимально допустимого (20):\n')
    for result in cur.execute("SELECT markets.title, items_num.itnum_quantity FROM markets INNER JOIN items_num ON markets.markets_id = items_num.itnum_id WHERE items_num.itnum_quantity < 20\n"):
       print(result)

    print('\n')
    print('Вывести список всех заявок магазинов, которые были сделаны в определенный период времени (2023.10.20 и 2022.03.05):\n')
    for result in cur.execute("SELECT markets.title, shop_applications.date_application FROM markets INNER JOIN shop_applications ON markets.markets_id = shop_applications.shap_id WHERE shop_applications.date_application = '2023.10.20' OR shop_applications.date_application = '2022.03.05'\n"):
       print(result)

    print('\n')
    print('Вывести список всех магазинов, у которых суммарное количество товаров на складе меньше заданного значения (25):\n')
    for result in cur.execute("SELECT markets.title, items_num.itnum_quantity FROM markets INNER JOIN items_num ON markets.markets_id = items_num.itnum_id GROUP BY markets.markets_id HAVING SUM(itnum_quantity) < 25\n"):
       print(result)
           

#Измененная таблица (Для Update)

if not os.path.exists('wholesale_base_changed.db'):
   with sq.connect('wholesale_base_changed.db') as con:
      con.execute('PRAGMA foreign_keys = ON')  # разрешает работу с внешними ключами
      cur = con.cursor()
      cur.execute("""CREATE TABLE items(
         items_id INTEGER PRIMARY KEY,
         title VARCHAR,
         description VARCHAR,
         unit VARCHAR
      )""")
      cur.execute("""CREATE TABLE markets(
         markets_id INTEGER PRIMARY KEY,
         title VARCHAR,
         address VARCHAR,
         telephone VARCHAR
      )""")
      cur.execute("""CREATE TABLE shop_applications(
         shap_id INTEGER PRIMARY KEY,
         markets_id INTEGER,
         date_application DATE,
         FOREIGN KEY (markets_id) REFERENCES markets(markets_id)
      )""")
      cur.execute("""CREATE TABLE items_num(
         itnum_id INTEGER PRIMARY KEY,
         items_id INTEGER,
         itnum_quantity INTEGER,
         FOREIGN KEY (items_id) REFERENCES items(items_id)
         )""")
      cur.execute("""CREATE TABLE composition(
         com_id INTEGER PRIMARY KEY,
         shap_id INTEGER KEY,
         items_id INTEGER,
         com_quantity INTEGER,
         FOREIGN KEY (shap_id) REFERENCES shop_applications(shap_id),
         FOREIGN KEY (items_id) REFERENCES items(items_id)
         )""")
      cur.executemany("INSERT INTO markets VALUES (?, ?, ?, ?)", markets)
      cur.executemany("INSERT INTO items VALUES (?, ?, ?, ?)", items)
      cur.executemany("INSERT INTO shop_applications VALUES (?, ?, ?)", shop_applications)
      cur.executemany("INSERT INTO items_num VALUES (?, ?, ?)", items_num)
      cur.executemany("INSERT INTO composition VALUES (?, ?, ?, ?)", composition)


with sq.connect('wholesale_base_changed.db') as con:
 con.execute('PRAGMA foreign_keys = ON')  
 cur = con.cursor()
 # 1. Обновить количество товара на складе для конкретного товара
 cur.execute('UPDATE items_num set itnum_quantity = 30 WHERE itnum_id = 6')
 #2. Обновить название товара в заявке
 cur.execute('UPDATE items set title = "Крутой окер" WHERE items_id = 3')
 #3. Обновить количество товара в заявке
 cur.execute('UPDATE items_num set itnum_quantity = 10 WHERE itnum_id = 1')
 #4. Обновить адрес магазина, который подал заявку
 cur.execute('UPDATE markets set address = "ул. Куйбышева, 200, Батайск, Ростовская обл., 346892" WHERE markets_id = 8')
 #5. Обновить дату заявки для конкретного магазина
 cur.execute('UPDATE shop_applications set date_application = "2022.08.17" WHERE markets_id = 5')
 #6. Обновить количество товара на складе для нескольких товаров
 cur.execute('UPDATE items_num set itnum_quantity = 0 WHERE itnum_id >= 9')
 #7. Обновить описание товара и количество на складе для конкретного товара
 cur.execute('UPDATE items SET description = "Семечки" WHERE items_id = 3')
 #8. Обновление количества товаров на складе, учитывая выполненную заявку магазина
 cur.execute('UPDATE items_num SET itnum_quantity = 60 WHERE itnum_id = 5')
 #9. Обновление количества товаров на складе, учитывая выполненную заявку магазина с учетом конкретного товара (Нужет 100% INNER JOIN, но у меня не получается сделать его с UPDATE)
 cur.execute('UPDATE items_num SET itnum_quantity = 80 WHERE itnum_id = 6')
 #10. Обновить название магазина в заявке, которую подал конкретный магазин
 cur.execute('UPDATE markets SET title = "Магнит" WHERE markets_id = 6')
 #11. Обновить адрес магазина и количество товара в заявке для конкретного товара
 cur.execute('UPDATE markets set address = "ул. Герцена 28, Батайск, Ростовская обл., 388892" WHERE markets_id = 6')
 cur.execute('UPDATE items_num SET itnum_quantity = 33 WHERE itnum_id = 4')
 #12. Обновить описание товара и количество на складе для нескольких товаров
 cur.execute('UPDATE items set description = "Газированная вода" WHERE items_id = 3 OR items_id = 4')
 cur.execute('UPDATE items_num SET itnum_quantity = 48 WHERE itnum_id = 7 OR itnum_id = 8')


#DELETE (Удаление данных из исходной таблицы)

if not os.path.exists('wholesale_base_delete.db'):
   with sq.connect('wholesale_base_delete.db') as con:
      con.execute('PRAGMA foreign_keys = ON')  # разрешает работу с внешними ключами
      cur = con.cursor()
      cur.execute("""CREATE TABLE items(
         items_id INTEGER PRIMARY KEY,
         title VARCHAR,
         description VARCHAR,
         unit VARCHAR
      )""")
      cur.execute("""CREATE TABLE markets(
         markets_id INTEGER PRIMARY KEY,
         title VARCHAR,
         address VARCHAR,
         telephone VARCHAR
      )""")
      cur.execute("""CREATE TABLE shop_applications(
         shap_id INTEGER PRIMARY KEY,
         markets_id INTEGER,
         date_application DATE NULL,
         FOREIGN KEY (markets_id) REFERENCES markets(markets_id)
      )""")
      cur.execute("""CREATE TABLE items_num(
         itnum_id INTEGER PRIMARY KEY,
         items_id INTEGER,
         itnum_quantity INTEGER,
         FOREIGN KEY (items_id) REFERENCES items(items_id)
         )""")
      cur.execute("""CREATE TABLE composition(
         com_id INTEGER PRIMARY KEY,
         shap_id INTEGER KEY,
         items_id INTEGER,
         com_quantity INTEGER,
         FOREIGN KEY (shap_id) REFERENCES shop_applications(shap_id),
         FOREIGN KEY (items_id) REFERENCES items(items_id)
         )""")
      cur.executemany("INSERT INTO markets VALUES (?, ?, ?, ?)", markets)
      cur.executemany("INSERT INTO items VALUES (?, ?, ?, ?)", items)
      cur.executemany("INSERT INTO shop_applications VALUES (?, ?, ?)", shop_applications)
      cur.executemany("INSERT INTO items_num VALUES (?, ?, ?)", items_num)
      cur.executemany("INSERT INTO composition VALUES (?, ?, ?, ?)", composition)

with sq.connect('wholesale_base_delete.db') as con: 
 cur = con.cursor()
 #1. Удаление заявки магазина и соответствующих записей в таблице состава:
 # Этот код вызовет ошибку, потому что в SQlite некоторые возможности недоступны как в обычном SQL (был бы он, ошибки бы не было)
 #cur.execute('DELETE shop_applications, composition FROM shop_applications INNER JOIN composition ON shop_applications.shap_id = composition.shap_id WHERE shop_applications.shap_id = 3')
 #2. Удалить из таблицы "Количество товаров на складе" записи, соответствующие товарам, не имеющим заявок в таблице "Состав"
 cur.execute('DELETE FROM items_num WHERE items_num.itnum_id IN (SELECT items_num.itnum_id FROM items_num INNER JOIN composition ON items_num.itnum_id = composition.items_id WHERE composition.com_quantity = 0)')
 #3. Удалить из таблицы "Заявки магазинов" все заявки магазинов, адрес которых начинается на "ул. Ленина" (поставлю свою!):
 cur.execute('DELETE FROM shop_applications WHERE markets_id IN (SELECT markets_id FROM markets WHERE address LIKE "ул. Гастелло%")')
 #4. Удалить из таблицы "Состав" записи, соответствующие товарам, которых нет на складе (количество = 0):
 cur.execute('DELETE FROM composition WHERE composition.items_id IN (SELECT composition.items_id FROM composition INNER JOIN items_num ON composition.items_id = items_num.items_id WHERE items_num.itnum_quantity = 0)')
 #5. Удалить из таблицы "Магазины" магазины, в которых не было заявок в течение последнего месяца:
 cur.execute('DELETE FROM markets WHERE markets.markets_id IN (SELECT markets.markets_id FROM markets INNER JOIN shop_applications ON markets.markets_id = shop_applications.markets_id WHERE shop_applications.date_application > "2023-02-01" OR shop_applications.date_application < "2023-02-30")')
 #7. Удалить из таблицы "Товары" товары, которые не были заказаны ни разу:
 cur.execute('DELETE FROM items WHERE items.items_id IN (SELECT items_num.items_id FROM items INNER JOIN items_num ON items.items_id = items_num.items_id WHERE items_num.itnum_quantity = 0)')
 #6. Удалить из таблицы "Количество товаров на складе" записи, соответствующие товарам, которые не были заказаны ни разу:
 cur.execute('DELETE FROM items_num WHERE items_num.itnum_id IN (SELECT items_num.itnum_id FROM items_num INNER JOIN markets ON items_num.itnum_id = markets.markets_id WHERE items_num.itnum_quantity = 0)')
 #7. Удалить из таблицы "Состав" записи, соответствующие заявкам, которые были поданы более месяца назад
 cur.execute('DELETE FROM composition WHERE composition.shap_id IN (SELECT composition.shap_id FROM composition INNER JOIN shop_applications ON composition.shap_id = shop_applications.shap_id WHERE shop_applications.date_application < "30.03.2023")')