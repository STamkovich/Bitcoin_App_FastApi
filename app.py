import fastapi
import database
import pydantic_models
import config

api = fastapi.FastAPI()

response = {"Ответ": "который возвращает сервер"}


@api.get('/')  # метод api.get() мы используем как декоратор при объявлении функции
def index():
    return response
