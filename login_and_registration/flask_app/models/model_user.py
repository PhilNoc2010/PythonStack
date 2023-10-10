from flask_app.config.mySQLconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app import EMAIL_REGEX, CHAR_REGEX



class User:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #C
    @classmethod
    def add_user(cls, data:dict) -> int:
        query = "INSERT INTO logins (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        user_id = connectToMySQL(DATABASE).query_db(query, data)
        return user_id

    #R
    @classmethod
    def get_user_by_email(cls, data:dict) -> dict:
        query = "SELECT * FROM logins WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        instance = results[0]
        user = cls(instance)
        return user


    #U

    #D

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 3:
            flash("First Name must be longer than 2 characters")
            is_valid = False
        if not CHAR_REGEX.match(user['first_name']):
            flash("First Name must contain only alphabetic characters")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last Name must be longer than 2 characters")
            is_valid = False
        if not CHAR_REGEX.match(user['last_name']):
            flash("Last Name must contain only alphabetic characters")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("email is not in a valid format")
            is_valid = False
        if len(user['password']) < 9:
            flash("Password must be longer than 8 characters")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Both password fields must match")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(user):
        is_valid = True
        print(user)
        if not EMAIL_REGEX.match(user['login_email']):
            flash("email is not in a valid format")
            is_valid = False
        if len(user['login_password']) < 9:
            flash("Password must be longer than 8 characters")
            is_valid = False
        return is_valid
