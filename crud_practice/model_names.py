# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database

class Name:
    DB = 'names'
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM names;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(Name.DB).query_db(query)
        # Create an empty list to append our instances of friends
        instance_list = []
        # Iterate over the db results and create instances of friends with cls.
        for dict in results:
            instance_list.append( cls(dict) )
        print(results)
        return instance_list

