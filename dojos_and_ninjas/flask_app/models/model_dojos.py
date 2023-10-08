from flask_app.config.mySQLconnection import connectToMySQL
from flask_app import DATABASE

class Dojo:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #C
    @classmethod
    def add_one(cls, data:dict) -> int:
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        dojo_id = connectToMySQL(DATABASE).query_db(query, data)
        return dojo_id

    #R
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # query = "SELECT * FROM dojos JOIN ninjas WHERE dojos.id = dojo_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        if not results:
            return []
        dojo_list = []
        for dict in results:
            dojo_list.append( cls(dict) )
        return dojo_list

    @classmethod
    def get_one(cls, data:dict):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        item = results[0]
        dojo = cls(item)
        return dojo

    #U

    #D
    @classmethod
    def delete_one(cls, data:dict):
        query = "DELETE FROM dojos WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
