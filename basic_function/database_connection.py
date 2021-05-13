from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
mysql_password = "dddd"
mysql_instance_name = "tt3"
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:' + mysql_password + '@localhost/' + mysql_instance_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'xxx'
db = SQLAlchemy(app)