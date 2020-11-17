from app import bcrypt,db
from bson import ObjectId

## banco de dados, oleções/trabelas ##
dbAdministradores = db['administradores']

class Tools():
    def __init__(self):
        pass

    def generate_password_hash(self, pwd):
        return bcrypt.generate_password_hash(pwd).decode('utf-8')
    
    def check_password_hash(self, pwdHash, pwd):
        return bcrypt.check_password_hash(pwdHash, pwd)
    
    def check_exist_db(self, id):
        dados = dbAdministradores.find_one({'_id': ObjectId(id)})
        if dados:
            return True
        else:
            return False

