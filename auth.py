from flask import Flask, jsonify, request
from flask.views import MethodView
from itsdangerous import URLSafeTimedSerializer as Serializer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'CChanGood!'


class AuthorToken(MethodView):
    def post(self):

        grant_type = request.args.get('grant_type')
        username = request.args.get('username')
        password = request.args.get('password')

        if grant_type is None or grant_type != 'password':
            response = jsonify(message=grant_type)
            response.status_code = 400
            return response

        if username != 'cchan' or password != '123':
            response = jsonify(message='wrong username or password!')
            response.status_code = 400
            return response

        s_timed = Serializer(app.config['SECRET_KEY'])
        res = s_timed.dumps([1,2,3])
        return res

    def get(self):
        content = request.args.get('content')
        s_timed = Serializer(app.config['SECRET_KEY'])
        res = s_timed.loads(content)

        return res


app.add_url_rule('/author_token/', view_func=AuthorToken.as_view('author_token'))

if __name__ == '__main__':
    app.run(debug=True)