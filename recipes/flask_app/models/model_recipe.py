from flask_app.config.mySQLconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import model_user


class Recipe:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.instruction = data['instruction']
        self.under_30_min = data['under_30_min']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #C
    @classmethod
    def add_recipe(cls, data:dict) -> int:
        query = "INSERT INTO recipes (title, description, instruction, under_30_min, user_id) values ( %(title)s, %(description)s, %(instruction)s, %(under_30_min)s, %(user_id)s);"
        recipe_id = connectToMySQL(DATABASE).query_db(query, data)
        return recipe_id

    #R
    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        if not results:
            return []
        recipe_list = []
        for dict in results:
            recipe_list.append( cls(dict) )
        return recipe_list

    @classmethod
    def get_all_joined_recipes(cls):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id ;"
        results = connectToMySQL(DATABASE).query_db(query)
        if not results:
            return []
        recipe_list = []
        for dict in results:
            recipe = cls(dict)
            user_data = {
                ** dict,
                'id' : dict['users.id'],
                'updated_at' : dict['users.updated_at'],
                'created_at' : dict['users.created_at']
            }
            user_instance = model_user.User(user_data)
            recipe.user_instance = user_instance
            recipe_list.append( recipe )
        return recipe_list

    @classmethod
    def get_one_recipe_joined(cls, data:dict):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return []
        item = results[0]
        recipe_instance = cls(item)
        user_data = {
            ** item,
            'id' : item['users.id'],
            'updated_at' : item['users.updated_at'],
            'created_at' : item['users.created_at']
        }
        user_instance = model_user.User(user_data)
        recipe_instance.user_instance = user_instance
        return recipe_instance

    @classmethod
    def get_recipe(cls, data:dict):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return []

        item = results[0]
        recipe_instance = cls(item)
        return recipe_instance

    #U
    @classmethod
    def update_recipe(cls, data:dict):
        query = "UPDATE recipes set title = %(title)s, description = %(description)s, instruction = %(instruction)s, under_30_min = %(under_30_min)s WHERE id = %(id)s;"
        print(query)
        recipe_id = connectToMySQL(DATABASE).query_db(query, data)
        return recipe_id

    #D
    @classmethod
    def delete_one_recipe(cls, data:dict):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        print(query)
        recipe_id = connectToMySQL(DATABASE).query_db(query, data)
        return recipe_id

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['title']) < 3:
            flash("Recipe Name must be longer than two characters")
            is_valid = False
        if len(recipe['description']) < 3:
            flash("Description must be longer than two characters")
            is_valid = False
        if len(recipe['instruction']) < 3:
            flash("instructions must be longer than two characters")
            is_valid = False
        return is_valid