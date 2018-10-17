from flask import Flask

app = Flask(__name__)

# run python 3 in the teminal
# from BooKModel import db
# db.create_all()
# exit()
# ls to view contents of the folder and see the newly created database.db
# cat database.db
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:////Users//onengiyerichard/Documents/pythonprojects/flaskproject//database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
