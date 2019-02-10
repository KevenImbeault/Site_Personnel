from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from sqlalchemy import create_engine
from json import dumps

e = create_engine('sqlite:///c:/sqlite/web.db')

app = Flask(__name__)
CORS(app)
api = Api(app)


class Github_Repos(Resource):
    def get(self):
        #Connect to database
        conn = e.connect()
        query = conn.execute ("select * from GITHUB")
        result = [dict(zip(tuple(query.keys()) ,i)) for i in query.cursor]
        return result

api.add_resource(Github_Repos, '/api/github')
    

if __name__ == '__main__':
    app.run(host='localhost')

