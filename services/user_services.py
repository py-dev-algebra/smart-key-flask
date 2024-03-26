from models.users import User


class UserServices:

    @classmethod
    def create_user(cls):
        pass

    @classmethod
    def get_user(cls) -> User:
        return User(first_name='Pero', last_name='Peric', pin_code='1234', is_active=False)

    @classmethod
    def update_user(cls):
        pass
    
    @classmethod
    def delete_user(cls):
        pass
