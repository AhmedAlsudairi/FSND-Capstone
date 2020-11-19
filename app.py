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

# @app.route('/movies', methods=['GET'])
# def get_drinks():
#     drinks = Drink.query.all()
#     formatedDrinks = [drink.short() for drink in drinks]
#     return jsonify({
#         'success': True,
#         'drinks': formatedDrinks
#     }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)