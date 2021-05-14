from flask import render_template,url_for,Flask
from flask_sqlalchemy import SQLAlchemy
import datetime
from basic_function.connection_dbModel import *
app = Flask(__name__)
mysql_password = "dddd"
mysql_instance_name = "tt3"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:' + mysql_password + '@localhost/' + mysql_instance_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/<int:id>')
def rount2(id):
    return str(PlayerName.query.filter(PlayerName.id == id).first().PlayerName)


if __name__ == '__main__':
    app.run(debug=True)
