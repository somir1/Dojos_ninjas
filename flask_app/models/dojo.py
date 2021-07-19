from flask_app.config.mysqlconnection import connectToMySQL

class Dojo():

    def __init__(self, data):
        self.id = data['id']
        self.name = data['dojo_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def show(cls):

        query = "SELECT * FROM dojos"

        results = connectToMySQL('dojos_schema').query_db(query)

        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos(dojo_name) VALUES (%(dojo_name)s);"

        return connectToMySQL('dojos_schema').query_db(query, data)

    @classmethod
    def dojo_with_id(cls, dojo_id):
        query = "SELECT * FROM dojos WHERE id = " + str(dojo_id) + ";"

        return connectToMySQL('dojos_schema').query_db(query)[0]