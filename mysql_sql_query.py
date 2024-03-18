from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import os

# dir
# --------------------------------------------------
basedir = os.path.abspath(os.path.dirname(__file__))

# flask
# --------------------------------------------------
app = Flask(__name__)
# https://docs.sqlalchemy.org/en/20/core/engines.html
# mysql://username:password@server/db
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:george0220@localhost:3306/test1"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.app_context().push()

db = SQLAlchemy(app)

sql = 'select * from agents'
result = db.session.execute(text(sql))
print(result.fetchall())

if __name__ == '__main__':
    app.run()