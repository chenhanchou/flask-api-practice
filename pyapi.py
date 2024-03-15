from flask import Flask, jsonify
from flask.views import MethodView

app = Flask(__name__)

# Method Based Dispatching
class API_Test(MethodView):
    def get(self) -> object:
        return jsonify(message='I am GET')

    def post(self) -> object:
        return jsonify(message='I am POST')
        
    def delete(self) -> object:
        return jsonify(message='I am DELETE')

app.add_url_rule('/test_api/', view_func=API_Test.as_view('test_api'))

# -------------------------------------------------------------
# origin method
# @app.route('/test_api/', methods=['GET'])
# def get(self):
#     return jsonify(message='I am GET')

# @app.route('/test_api/', methods=['POST'])
# def post(self):
#     return jsonify(message='I am POST')

# @app.route('/test_api/', methods=['DELETE'])
# def delete(self):
#     return jsonify(message='I am DELETE')
# --------------------------------------------------------------
if __name__ == '__main__':
    app.run()