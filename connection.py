from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://snrmyrdk:WdWoPvt6qtVm9uq8V93rSYGKkf3WW-nt@tuffi.db.elephantsql.com/snrmyrdk'

db = SQLAlchemy(app)
