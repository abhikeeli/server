from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db = SQLAlchemy(app)

from models import Drink
    
@app.route('/')
def index():
    return 'Hello!'
@app.route('/drinks')
def get_drinks():
    drinks=Drink.query.all()
    output=[]
    for drink in drinks:
        drink_data={'name':drink.name , 'description':drink.description}
        output.append(drink_data)
    return{"drink":output}
@app.route('/drinks/<id>')
def get_onedrink(id):
    drink=Drink.query.get_or_404(id)
    return{'name':drink.name , 'description':drink.description}
@app.route('/drinks', methods=['POST'])
def new_drink():
    drink=Drink(name=request.json['name'],description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'<id>':drink.id}

@app.route('/drinks/<id>', methods=['DELETE'])
def rem_drink(id):
    print(id)
    drink=Drink.query.get(id)
    if drink is None:
        return {"error":"notfound"}
    db.session.delete(drink)
    db.session.commit()
    return {"status":"deleted"}
