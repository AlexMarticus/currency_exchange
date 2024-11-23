from src.auth.models import Users
from src.base_repository import Repository


class UserRepository(Repository):
    model = Users