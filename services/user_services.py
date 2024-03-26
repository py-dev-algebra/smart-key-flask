from models.users import User
from repositories.file_repository import FileRepo


class UserServices:

    @classmethod
    def create_user(cls, user: User):
        return FileRepo.save_to_file(str(user))

    @classmethod
    def get_user(cls) -> User:
        return User(first_name='Pero', last_name='Peric', pin_code='1234', is_active=False)

    @classmethod
    def update_user(cls):
        pass
    
    @classmethod
    def delete_user(cls):
        pass
