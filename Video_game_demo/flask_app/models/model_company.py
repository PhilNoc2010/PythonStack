from flask_app.config.mySQLconnection import connectToMySQL

class Company:
    DB = 'video_games_db'
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    ## C
    @classmethod
    def add_one(cls, data:dict) -> int:
        query = "INSERT INTO companys (name) VALUES (%(name)s);"
        company_id = connectToMySQL(Company.DB).query_db(query, data)
        return company_id

    ## R
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM companys;"
        results = connectToMySQL(Company.DB).query_db(query)
        ## Shield to prevent invalid search from crashing the server
        if (results == False):
            return []
        instance_list = []
        for dict in results:
            instance_list.append( cls(dict) )
        return instance_list

    @classmethod
    def get_one(cls, data:dict):
        query = "SELECT * FROM companys WHERE id = %(id)s;"
        results = connectToMySQL(Company.DB).query_db(query,data)
        if (results == False):
            return False
        item = results[0]
        instance = cls(item)
        return instance

    ## U

    ## D
    @classmethod
    def remove_game(cls, data:dict):
        print(data)
        query = "DELETE FROM companys WHERE id = %(id)s;"
        connectToMySQL(Company.DB).query_db(query, data)
