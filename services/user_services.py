from typing import List
from models.users import User
from repositories.file_repository import FileRepo


class UserServices:

    @classmethod
    def create_user(cls, user: User):
        return FileRepo.save_to_file(str(user))

    @classmethod
    def get_users(cls) -> List[User]:
        users_from_file = FileRepo.read_from_file()
        users_list = []
        for line in users_from_file:
            user_props = line.split(';')
            user_props[3] = user_props[3].strip()
            user_props[3] = user_props[3].replace('\n', '')
            if user_props[3] == 'Aktivan':
                users_list.append(User(first_name=user_props[0], last_name=user_props[1], pin_code=user_props[2], is_active=True))
            else:
                users_list.append(User(first_name=user_props[0], last_name=user_props[1], pin_code=user_props[2], is_active=False))

        return users_list


    @classmethod
    def update_user(cls):
        pass
    
    @classmethod
    def delete_user(cls):
        pass
