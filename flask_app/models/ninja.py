from flask_app.config.mysqlconnection import connectToMySQL

class Ninja ():

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas(first_name, last_name, age, dojo_id) VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"

        return connectToMySQL('dojos_schema').query_db(query, data)
        
    @classmethod
    def get_ninjas_with_dojo_id(cls, dojo_id):

        query = "SELECT * FROM ninjas JOIN dojos ON id = ninjas.dojo_id WHERE dojo_id =" + str(dojo_id) + ";"
        return connectToMySQL('dojos_schema').query_db(query)
