from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session, sessionmaker
from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, SmallInteger
from sqlalchemy.ext.declarative import declarative_base

#engine = create_engine("postgresql+psycopg2://postgres:1111@localhost/sqlalchemy_tuts")
engine = create_engine("postgresql+psycopg2://postgres:Ваш_пароль@localhost/sqlalchemy_tuts")
session = Session(bind=engine)
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
q = session.query(Customer)

menu = ["Первый", "Второй", "Третий"]
app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', title = 'Про Flask', menu = menu)
@app.route('/about')
def about():
    return render_template('about.html', title = 'О сайте')

@app.route('/customer')
def customer():
    return render_template('customer.html', title = 'Customers', list = q)
@app.route('/help')
def help():
    return render_template('help.html')

if __name__ == "__main__":
    app.run(debug=True)