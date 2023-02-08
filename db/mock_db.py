from utils.util import Singleton

class Database(metaclass=Singleton):
    
    product_table = []
    user_table = []