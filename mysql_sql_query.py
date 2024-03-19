from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.sql import text

# flask
# --------------------------------------------------
app = Flask(__name__)
# https://docs.sqlalchemy.org/en/20/core/engines.html
# mysql://username:password@server/db
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:george0220@localhost:3306/test1"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["SQLALCHEMY_ECHO"] = True
engine_url = "mysql+pymysql://root:george0220@localhost:3306/test1"
engine = create_engine(engine_url, echo=True)

with engine.connect() as connection:
    sql = 'select * from agents'
    result = connection.execute(text(sql))
    for row in result:
        print("username:", row.AGENT_NAME)

if __name__ == '__main__':
    app.run()