from flask import Flask, jsonify, request, make_response
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin


app = Flask(__name__)
api=Api(app)

db = SQLAlchemy(app)
db.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECURITY_PASSWORD_SALT'] = 'my_precious_two'
app.config['SECRET_KEY'] = 'my_precious'

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean(), default=True)
    
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    fs_token_uniquifier = db.Column(db.String(255), unique=True, nullable=True)

    roles = db.relationship('Roles', secondary='user_roles')
    

class Roles(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255))

class UserRoles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


user_datastore = SQLAlchemyUserDatastore(db, Users, Roles)
security = Security(app, user_datastore)



# role = Roles.filter_by(name='admin').first()


# user = Users(
#     email = 'admin@gmail.com',
#     password = 'admin123',
#     roles = [role],
# )
# db.session.add(user)
# db.session.commit()

# get_user = Users.query.filter_by(email = "admin@gmail.com").first()
# role = Roles.query.filter_by(name='admin').first()

# userrole = UserRoles(
#     user_id = get_user.id,
#     role_id = role.id
# )

# db.session.add(userrole)
# db.session.commit()





database = []

class UserDetails(Resource):
    def get(self):
        return make_response(jsonify(database),200)
    
    def post(self):
        user_details = request.get_json()
        print(user_details)
        if not user_details:
            return jsonify({'error': 'No user details provided'})
        else:
            database.append(user_details)
            return jsonify({'message': 'User added successfully', 'user': user_details})
        
    def delete(self, str1, str2):
        len1 = len(str1)
        len2 = len(str2)
        result = {
            'total_length': len1 + len2,
        }

        return make_response(jsonify(result), 203)
        
api.add_resource(UserDetails, '/api/users', '/api/users/<string:str1>/<string:str2>')


@app.route('/api/get_users' , methods = ['GET'])
def get_users():
    return jsonify(database)

@app.route('/api/add_user', methods=['POST'])
def add_user():
    user_details = request.get_json()
    if not user_details:
        return jsonify({'error': 'No user details provided'}), 400
    else:
        database.append(user_details)
        return jsonify({'message': 'User added successfully', 'user': user_details}), 201
    

@app.route('/api/hello_world', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, World!'})

@app.route('/api/<string:str1>/<string:str2>')
def get_length(str1, str2):
    length1 = len(str1)
    length2 = len(str2)
    result = {
        'total_lenght' : length1 + length2,
    }

    return jsonify(result) , 203




if __name__ == '__main__':
    app.run(debug=True)