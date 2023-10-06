from flask_app.config.mySQLconnection import connectToMySQL

class Game:
    DB = 'video_games_db'
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.name = data['name']
        self.genre = data['genre']
        self.rating = data['rating']
        self.release_year = data['release_year']
        self.company = data['company']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    ## C
    @classmethod
    def add_one(cls, data:dict):
        query = "INSERT INTO games ( name, genre, rating, release_year, company) VALUES (%(name)s, %(genre)s, %(rating)s, %(release_year)s, %(company))s); "
        game_id = connectToMySQL(Game.DB).query_db(query)
        return game_id

    ## R
    @classmethod
    def get_all(cls):
        query = "SELECT * from games;"
        results = connectToMySQL(Game.DB).query_db(query)
        ## Shield to prevent invalid searches from crashing the server
        if (results == False):
            return []
        instance_list = []
        for dict in results:
            instance_list.append( cls(dict) )
        print(results)
        return instance_list

    ## U

    ## D