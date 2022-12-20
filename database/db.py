from pony.orm import *

db = Database()


# создаём модели (Сущностей (Entity на английском)

class User(db.Entity):
    """Пользователь"""
    user_id = Required(str)
    nick = Required(str)
    age = Required(int)
    wallets = Set('Wallet')


class Wallet(db.Entity):
    """Кошелёк"""
    address = Required(str)
    private_key = Required(str)
    owner = Required(User)

# Database.bind(). Он используется для привязки объявленных сущностей к определенной базе данных
# filename=':memory:' - для хранения бд в памяти
try:
    db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
except Exception as Ex:
    print(Ex)
# db.generate_mapping(create_tables=True)
# Параметр create_tables=True указывает, что если таблицы еще не существуют,
# то они будут созданы с помощью команды CREATE TABLE

