from db.mock_db import Database


class User:

    def __init__(self, name: str = None, telephone: str = None, address_state: str = None) -> None:
        self.name = name
        self.telephone = telephone
        self.address_state = address_state
    
    def insert(self):
        if not self.name or not self.telephone or not self.address_state:
            raise 'User fields must not be None.'
        
        new_user = {'name': self.name,'telephone': self.telephone, 'address_state': self.address_state }
        Database().user_table.append(new_user)

        return new_user

    def get_all(self):
        return Database().user_table

    def filter_by_state(self, address_state) -> list: 
        filtered_users = []
        for user in Database().user_table:
            if user.get('address_state') == address_state:
                filtered_users.append(user)

        return filtered_users