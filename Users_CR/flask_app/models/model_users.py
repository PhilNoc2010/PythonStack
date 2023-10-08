from flask_app.config.mySQLconnection import connectToMySQL
from flask_app import DATABASE

class User:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #C
    @classmethod
    def add_one(cls, data:dict) -> int:
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        user_id = connectToMySQL(DATABASE).query_db(query, data)
        return user_id

    #R
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        if not results:
            return []
        instance_list = []
        for dict in results:
            instance_list.append( cls(dict) )
        return instance_list

#U

#D
