import fastapi
import database
import pydantic_models
import config

api = fastapi.FastAPI()

# @api.get('/static/path')
# def hello():
#     return "hello"
#
#
# @api.get('/user/{nick}')  # переменные в пути заключаются в фигурные скобки
# def get_nick(nick):  # в функцию передаем эту переменную и работаем с ней дальше
#     return {"user": nick}  # при запросе страницы вернет строку, которую мы вписали после последнего слеша
#

# @api.get('/userid/{id:int}')  # мы можем задавать тип данных прямо в пути через двоеточие
# def get_id(id):  # тут в пути обязательно должно быть число, иначе возникнет ошибка
#     return {"user": id}
#
#
# @api.get('/user_id/{id}')
# def get_id2(id: int):  # либо же его можно задавать как тайп-хинт прямо в функции
#     return {"user": id}  # возвращается число, а не строка, как было бы без объявления типа данных
#
#
# @api.get('/user_id_str/{id:str}')
# def get_id2(id):
#     return {"user": id}  # тут id - это уже строка, так как мы объявили тип данных
#
#
# @api.get('/test/{id:int}/{text:str}/{custom_path:path}')
# def get_test(id, text, custom_path):
#     return {"id": id,
#             "": text,
#             "custom_path": custom_path}

fake_database = {'users': [
    {
        "id": 1,  # тут тип данных - число
        "name": "Anna",  # тут строка
        "nick": "Anny42",  # и тут
        "balance": 15300  # а тут float
    },

    {
        "id": 2,  # у второго пользователя
        "name": "Dima",  # такие же
        "nick": "dimon2319",  # типы
        "balance": 160.23  # данных
    }
    , {
        "id": 3,  # у третьего
        "name": "Vladimir",  # юзера
        "nick": "Vova777",  # мы специально сделаем
        "balance": "25000"  # нестандартный тип данных в его балансе
    }
], }


@api.get('/get_info_by_user_id/{id:int}')
def get_info_about_user(id):
    return fake_database['users'][id - 1]


@api.get('/get_user_balance_by_id/{id:int}')
def get_user_balance(id):
    return fake_database['users'][id - 1]['balance']


@api.get('/get_total_balance')
def get_total_balance():
    total_balance: float = 0.0
    for user in fake_database['users']:
        total_balance += pydantic_models.User(**user).balance  # проверка на валидность с помощью pydantic
    return total_balance


# обработка get запроса с параметрами
# skip - пропускает количество записей
# limit - ставит ограничения
@api.get("/users/")
def get_users(skip: int = 0, limit: int = 10):
    return fake_database['users'][skip: skip + limit]

# Когда мы задаем аргументы в функции обработки запроса мы можем им дать значения по умолчанию,
# причем делая это с применением тайп-хинтов. Если один из параметров совсем необязателен,
# то можно сделать так:

@api.get("/user/{user_id}")
def read_user(user_id: str, query: str | None = None):
    """
    Тут значение по умолчанию для query будет None
    """
    if query:
        return {"user_id": user_id, "query": query}
    return {"user_id": user_id}
