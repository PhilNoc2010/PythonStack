from flask_app.config.mySQLconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import model_dojos

class Ninja:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_one(cls, data:dict) -> int:
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        ninja_id = connectToMySQL(DATABASE).query_db(query, data)
        return ninja_id

    @classmethod
    def get_all_by_dojo(cls,data:dict) -> list:
        query = "SELECT * from ninjas JOIN dojos ON dojos.id = dojo_id WHERE dojo_id = %(dojo_id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return []
        ninjas = []
        for ninja in results:
            print(ninja)
            ninjas.append(cls(ninja))
        print(ninjas)
        return ninjas