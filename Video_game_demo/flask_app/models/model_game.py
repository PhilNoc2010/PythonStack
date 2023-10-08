from flask_app.config.mySQLconnection import connectToMySQL
from flask_app.models import model_company

class Game:
    DB = 'video_games_db'
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.name = data['name']
        self.genre = data['genre']
        self.rating = data['rating']
        self.release_year = data['release_year']
        self.company_id = data['company_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    ## C
    @classmethod
    def add_one(cls, data:dict) -> int:
        query = "INSERT INTO games (name, genre, rating, release_year, company_id) VALUES (%(name)s, %(genre)s, %(rating)s, %(release_year)s, %(company_id)s);"
        game_id = connectToMySQL(Game.DB).query_db(query, data)
        return game_id

    ## R
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM games;"
        results = connectToMySQL(Game.DB).query_db(query)
        ## Shield to prevent invalid searches from crashing the server
        if (results == False):
            return []
        instance_list = []
        for dict in results:
            instance_list.append( cls(dict) )
        return instance_list

    @classmethod
    def get_one(cls, data:dict):
        # query = "SELECT * FROM games WHERE id = %(id)s;"
        query = "SELECT * from games JOIN companys ON games.company_id = companys.id WHERE games.id = %(id)s;"
        results = connectToMySQL(Game.DB).query_db(query, data)
        print(results)
        if (results == False):
            return False

        item = results[0]
        game_instance = cls(item)

        ## extract conflicting columns from the return object
        company_data = {
            ## resolving conflicting columns from SQL Query
            'id': item['companys.id'],
            'created_at': item['companys.created_at'],
            'updated_at': item['companys.updated_at'],
            'name': item['companys.name']
        }
        ## create company instance
        company_instance = model_company.Company(company_data)

        ## attach company data
        game_instance.company = company_instance
        print(game_instance.company)
        return game_instance

    ## U

    ## D
    @classmethod
    def remove_game(cls, data:dict):
        query = "DELETE FROM games WHERE id = %(id)s;"
        connectToMySQL(Game.DB).query_db(query, data)

    ## validators
    @staticmethod
    def validator(data:dict) -> bool:
        is_valid = True

        if(len(data['name']) < 2):
            print("Name must be longer than 2 characters")
            is_valid = False

