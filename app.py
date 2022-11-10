from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource
from aproc import x, valid_y, get_data

app = Flask(__name__)
cors = CORS(app, origins=["http://localhost:3000"])
api = Api(app)


class Index(Resource):
    def get(self):
        rnd_y, aproc_y = get_data()
        return {
            'valid_func': {
                'x': [round(xi, 3) for xi in x],
                'y': [round(yi, 3) for yi in valid_y]
            },

            'aproc_func': {
                'x': [round(xi, 3) for xi in x],
                'y': [round(yi, 3) for yi in aproc_y]
            },

            'rnd_dots': {
                'x': [round(xi, 3) for xi in x],
                'y': [round(yi, 3) for yi in rnd_y]
            },
        }


api.add_resource(Index, '/api/result')

if __name__ == '__main__':
    app.run(debug=True)
