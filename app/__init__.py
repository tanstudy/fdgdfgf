from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.secret_key = '^%*&^^HJGHJGHJFD%^&%&*^*(^^^&^(*^^$%^GHJFGHJH'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saledbv1?charset=utf8mb4" % quote('1234')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 6

db = SQLAlchemy(app=app)
login = LoginManager(app=app)

import cloudinary

cloudinary.config(
    cloud_name="dxxwcby8l",
    api_key="448651448423589",
    api_secret="ftGud0r1TTqp0CGp5tjwNmkAm-A"
)
