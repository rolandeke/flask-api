# import modules 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields,marshal_with, abort

# create flask app instance 
app = Flask(__name__)

#add db connection string to app config
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

# instanciate database 
db = SQLAlchemy(app)

# create an api instance from flask_restful and pass 
# the flask app as input parameter
api = Api(app)

# create a user model 
class UserModel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  email = db.Column(db.String(80), unique=True, nullable=False)
  
  def __repr__(self):
    return f"User(name = {self.name}, email = {self.email})"

# create request argument parser
user_args = reqparse.RequestParser()
# add expected request fields to the parser
user_args.add_argument('name', type=str, required=True, help="Name is required")
user_args.add_argument('email', type=str, required=True, help="Email is required")


userFields = {
  'id':fields.Integer,
  'name':fields.String,
  'email':fields.String,
}


class Users(Resource):
  @marshal_with(userFields)
  def get(self):
    users = UserModel.query.all()
    return users
  
  @marshal_with(userFields)
  def post(self):
    args = user_args.parse_args()
    user = UserModel(name=args["name"], email=args["email"])
    db.session.add(user)
    db.session.commit()
    users = UserModel.query.all()
    return users, 201
  
class User(Resource):
  @marshal_with(userFields)
  def get(self,id):
    user = UserModel.query.filter_by(id=id).first()
    if not user:
      abort(404)
    return user
  
  @marshal_with(userFields)
  def patch(self,id):
    args = user_args.parse_args()
    user = UserModel.query.filter_by(id=id).first()
    if not user:
      abort(404)
    user.name = args["name"]
    user.email = args["email"]
    db.session.commit()
    return user
  
  @marshal_with(userFields)
  def delete(self,id):
    user = UserModel.query.filter_by(id=id).first()
    if not user:
      abort(404)
    db.session.delete(user)
    db.session.commit()
    users = UserModel.query.all()
    return users, 204
  
api.add_resource(Users,'/api/users/')
api.add_resource(User,'/api/users/<int:id>')
    
@app.route("/")
def home():
  return '<h1>Flask rest ap</h1>'




if __name__ == "__main__":
  app.run(debug=True)