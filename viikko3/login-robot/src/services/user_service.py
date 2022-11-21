from entities.user import User
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa

        if not re.match("^[a-z]{3,}$", username):
            raise UserInputError("Username should be 3+ letters from a to z")

        if (not re.match("^[a-z0-9]{8,}$", password) 
        or not re.match("^.*[0-9]+.*$", password)
        or not re.match("^.*[a-z]+.*$", password)
            ):
            raise UserInputError("Username should be length 8 or more and contain letter a-z and digits.")
