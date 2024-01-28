from app.config import database
from .repository.repository import History


class Service:
    def __init__(self):
        self.repository = History(database)

def get_service():
    svc = Service()
    return svc
