from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users
            
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        result = connectToMySQL('users_schema').query_db( query, data )
        return result
    
    @staticmethod
    def validate_users():
        is_valid = True
        if len(request.form['first_name']) <= 0:
            flash("First Name must be at least two letters long")
            is_valid = False
        if len(request.form['last_name']) <= 0:
            flash("Last Name must be at least two letters long")
            is_valid = False
        return is_valid