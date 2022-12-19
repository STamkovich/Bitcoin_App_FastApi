import pydantic

# создаём модель

class User(pydantic.BaseModel):
    id: int
    name: str
    nick: str
    balance: float