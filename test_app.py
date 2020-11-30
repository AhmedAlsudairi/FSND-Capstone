import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie

CASTING_ASSISTANCE = ''
EXECUTIVE_PRODUCER_TOKEN = ''
CASTING_DIRECTOR_TOKEN = ''


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the casting agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_agency_test"
        self.database_path = "postgres://{}:{}@{}/{}".format(
            'postgres', 'admin', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        actor = Actor(name="khalid", age=50, gender="male")
        actor.insert()
        movie = Movie(title="Attack on titan", release_date="2020-12-12")
        movie.insert()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_get_actors(self):
        response = self.client().get(
            '/actors', headers={"Authorization": f"{CASTING_ASSISTANCE}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_get_actors_error(self):
        response = self.client().get(
            '/actors?page=500', headers={"Authorization": f"{CASTING_ASSISTANCE}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], "Not Found")

    def test_get_movies(self):
        response = self.client().get(
            '/movies', headers={"Authorization": f"{CASTING_ASSISTANCE}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_get_movies_error(self):
        response = self.client().get(
            '/movies?page=500', headers={"Authorization": f"{CASTING_ASSISTANCE}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], "Not Found")

    def test_delete_actor(self):
        response = self.client().delete(
            '/actors/1', headers={"Authorization": f"{CASTING_DIRECTOR_TOKEN}"})
        data = json.loads(response.data)

        actor = Actor.query.get(1)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 1)
        self.assertTrue(data['total_actors'])
        self.assertEqual(actor, None)

    def test_delete_actor_error(self):
        response = self.client().delete(
            '/actors/1000', headers={"Authorization": f"{CASTING_DIRECTOR_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], "Not Found")

    def test_delete_movie(self):
        response = self.client().delete(
            '/movies/1', headers={"Authorization": f"{EXECUTIVE_PRODUCER_TOKEN }"})
        data = json.loads(response.data)

        movie = Actor.query.get(1)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 1)
        self.assertTrue(data['total_movies'])
        self.assertEqual(movie, None)

    def test_delete_movie_error(self):
        response = self.client().delete(
            '/movies/1000', headers={"Authorization": f"{EXECUTIVE_PRODUCER_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], "Not Found")

    def test_post_actor(self):
        response = self.client().post('/actors',
                                      json={'name': 'Ahmed', 'age': 22, 'gender': 'male'}, headers={"Authorization": f"{CASTING_DIRECTOR_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_actors'])

    def test_post_actor_error(self):
        response = self.client().post('/actors',
                                      json={'firstName': 'Ahmed', 'age': 22, 'gender': 'male'}, headers={"Authorization": f"{CASTING_DIRECTOR_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], "Bad Request")

    def test_post_movie(self):
        response = self.client().post('/movies',
                                      json={'title': 'Toy Story', 'release_date': '2020-12-12'}, headers={"Authorization": f"{EXECUTIVE_PRODUCER_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_movies'])

    def test_post_movie_error(self):
        response = self.client().post('/movies',
                                      json={'movieTitle': 'Toy Story', 'release_date': '2020-12-12'}, headers={"Authorization": f"{EXECUTIVE_PRODUCER_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], "Bad Request")

    def test_patch_actor(self):
        response = self.client().patch('/actors/1',
                                      json={'name': 'Saleh', 'age': 45, 'gender': 'male'}, headers={"Authorization": f"{CASTING_DIRECTOR_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_patch_actor_error(self):
        response = self.client().patch('/actors/1',
                                      json={'firstName': 'Saleh', 'age': 45, 'gender': 'male'}, headers={"Authorization": f"{CASTING_DIRECTOR_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], "Bad Request")

    def test_patch_movie(self):
        response = self.client().patch('/movies/1',
                                      json={'title': 'Toy Story', 'release_date': '2020-12-12'}, headers={"Authorization": f"{EXECUTIVE_PRODUCER_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_patch_movie_error(self):
        response = self.client().patch('/movies/1',
                                      json={'movieTitle': 'Toy Story', 'release_date': '2020-12-12'}, headers={"Authorization": f"{EXECUTIVE_PRODUCER_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], "Bad Request")
        
    # def test_search_question(self):
    #     response = self.client().post('/questions/search', json={'searchTerm': 'which'})
    #     data = json.loads(response.data)

    #     self.assertEqual(response.status_code,200)
    #     self.assertEqual(data['success'],True)
    #     self.assertTrue(len(data['questions']))
    #     self.assertTrue(data['total_questions'])
    #     self.assertEqual(data['current_category'],None)

    # def test_400_if_search_question_bad_request(self):
    #     response = self.client().post('/questions/search', json={'search': 'which'})
    #     data = json.loads(response.data)

    #     self.assertEqual(response.status_code,400)
    #     self.assertEqual(data['success'],False)
    #     self.assertTrue(data['message'],"Bad Request")

    # def test_get_questions_by_category(self):
    #     response = self.client().get('/categories/1/questions')
    #     data = json.loads(response.data)
    #     category = Category.query.get(1)

    #     self.assertEqual(response.status_code,200)
    #     self.assertEqual(data['success'],True)
    #     self.assertTrue(len(data['questions']))
    #     self.assertTrue(data['total_questions'])
    #     self.assertEqual(data['current_category'],category.type)

    # def test_404_sent_requesting_beyond_valid_categories(self):
    #     response = self.client().get('/categories/1000/questions')
    #     data = json.loads(response.data)

    #     self.assertEqual(response.status_code,404)
    #     self.assertEqual(data['success'],False)
    #     self.assertTrue(data['message'],"Not Found")

    # def test_get_question_quizzes(self):
    #     category = Category.query.get(4)
    #     questions = Question.query.filter_by(category=category.id).all()

    #     previous_questions = [question.id for question in questions]

    #     response = self.client().post('/quizzes', json={"quiz_category": category.format(), "previous_questions": previous_questions})
    #     data = json.loads(response.data)

    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['success'], True)

    # def test_400_get_question_quizzes_bad_request(self):
    #     category = Category.query.get(4)
    #     questions = Question.query.filter_by(category=category.id).all()

    #     previous_questions = [question.id for question in questions]

    #     response = self.client().post('/quizzes', json={"category": category.format(), "questions": previous_questions})
    #     data = json.loads(response.data)

    #     self.assertEqual(response.status_code,400)
    #     self.assertEqual(data['success'],False)
    #     self.assertTrue(data['message'],"Bad Request")
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
