from flask import Flask
from flask_restx import Api
from views.perform_query import perform_query_ns


app = Flask(__name__)
api = Api(app)
api.add_namespace(perform_query_ns)

if __name__ == '__main__':
    app.run(debug=True)
