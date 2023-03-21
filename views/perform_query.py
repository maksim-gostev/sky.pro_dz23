import os

from flask import request
from flask_restx import Resource, Namespace

from utils import execute

perform_query_ns = Namespace('perform_query')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "../data")

@perform_query_ns.route('')
class Perform_query(Resource):
    def post(self):
        req_json = request.json

        if "query" not in req_json.keys() or "file_name" not in req_json.keys():
            return "Проверьте запрос или имя файла"

        filename = os.path.join(DATA_DIR, req_json["file_name"])

        if not os.path.exists(filename):
            return 'Фаила не существует'

        query = req_json["query"]
        return execute(query, filename)

