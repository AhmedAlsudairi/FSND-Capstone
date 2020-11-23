import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movie, Actor, Role


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)
    setup_db(app)
    return app


app = create_app()


@app.route('/actors', methods=['GET'])
def get_actors():
    try:
        actors = Actor.query.order_by(Actor.id).all()
        formated_actors = [actor.format() for actor in actors]
        print(formated_actors)
        return jsonify({
            "success": True,
            "actors": formated_actors
        })
    except:
        abort(422)


@app.route('/actors', methods=['POST'])
def post_actor():
    try:
        body = request.get_json()

        name = body['name']
        age = body['age']
        gender = body['gender']
        actor = Actor(name=name, gender=gender, age=age)
        print(actor.name)
        actor.insert()

        return jsonify({
            "success": True,
            "created": actor.id,
            "total_actors": len(Actor.query.all())
        })
    except:
        abort(400)


@app.route('/movies', methods=['GET'])
def get_movies():
    try:
        movies = Movie.query.order_by(Movie.id).all()
        formated_movies = [movie.format() for movie in movies]
        print(formated_movies)
        return jsonify({
            "success": True,
            "movies": formated_movies
        })
    except:
        abort(422)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
