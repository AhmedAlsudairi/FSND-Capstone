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


@app.route('/actors/<int:actor_id>', methods=['DELETE'])
def delete_actor(actor_id):
    try:
            query = Actor.query.get(actor_id)
            query.delete()
            return jsonify({
                "success": True,
                "deleted": actor_id,
              "total_actors": len(Actor.query.all())
            })
    except:
            abort(404)


@app.route('/actors', methods=['POST'])
def post_actor():
    try:
        body = request.get_json()

        name = body['name']
        age = body['age']
        gender = body['gender']
        actor = Actor(name=name, gender=gender, age=age)
        actor.insert()

        return jsonify({
            "success": True,
            "created": actor.id,
            "total_actors": len(Actor.query.all())
        })
    except:
        abort(400)


@app.route('/actors/<int:actor_id>', methods=['PATCH'])
def update_actor(actor_id):
    data = request.get_json()
    name = data.get('name', None)
    age = data.get('age', None)
    gender = data.get('gender', None)
    try:
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if actor is None:
            abort(404)

        if name is None:
            abort(400)

        if name is not None:
            actor.name = name

        if age is not None:
            actor.age = age

        if gender is not None:
            actor.gender = gender
        print(actor.name)
        print(actor.age)
        print(actor.gender)
        actor.update()

        actors = Actor.query.order_by(Actor.id).all()
        formated_actors = [actor.format() for actor in actors]

        return jsonify({
            'success': True,
            'actors': formated_actors
        }), 200
    except:
        abort(422)

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


@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    try:
            query = Movie.query.get(movie_id)
            query.delete()
            return jsonify({
                "success": True,
                "deleted": movie_id,
              "total_movies": len(Movie.query.all())
            })
    except:
            abort(404)


@app.route('/movies', methods=['POST'])
def post_movie():
    try:
        body = request.get_json()

        title = body['title']
        release_date = body['release_date']
        movie = Movie(title=title, release_date=release_date)
        movie.insert()

        return jsonify({
            "success": True,
            "created": movie.id,
            "total_movies": len(Movie.query.all())
        })
    except:
        abort(400)

@app.errorhandler(422)
def unprocessable_entity(error):
    return jsonify({
      "success" : False,
      "status_code" : 422,
      "message" : "Unprocessable Entity"
    }), 422

@app.errorhandler(404)
def not_found(error):
    return jsonify({
      "success" : False,
      "status_code" : 404,
      "message" : "Not Found"
    }), 404  

@app.errorhandler(400)
def bad_request(error):
    return jsonify({
      "success" : False,
      "status_code" : 400,
      "message" : "Bad Request"
    }), 400  

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
