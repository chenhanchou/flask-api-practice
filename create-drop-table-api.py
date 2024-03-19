from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer, String, DATETIME
from flask import Flask, jsonify
from flask.views import MethodView

Base = declarative_base()
engine_url = "mysql+pymysql://root:root@localhost:3306/test1"
engine = create_engine(engine_url, echo=True)

class Test(Base):
    __tablename__ = "test1"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(15))
    time = Column(DATETIME)


def create_table():
    Test.metadata.create_all(engine)


def drop_table():
    Test.metadata.drop_all(engine)


app = Flask(__name__)
class API_Test(MethodView):
    def post(self) -> object:
        try:
            create_table()
            resp = jsonify(message='success!',success=True)
            return resp
        except:
            resp = jsonify(message='fail!',success=False)
            return resp
        
    def delete(self) -> object:
        try:
            drop_table()
            resp = jsonify(message='success!',success=True)
            return resp
        except:
            resp = jsonify(message='fail!',success=False)
            return resp

app.add_url_rule('/test/', view_func=API_Test.as_view('test'))
    


if __name__ == '__main__':
    app.run(debug=True)