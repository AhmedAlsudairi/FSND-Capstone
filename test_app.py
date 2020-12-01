import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie

CASTING_ASSISTANCE_TOKEN = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImV1N0FSUGxQUVZDRlRpYlFGUkllSSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYWhtZWQtYWxzdWRhaXJpLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmM1MmEwNTYxZjllNzAwNzY4OTdmNzciLCJhdWQiOiJjYXN0aW5nIF9hZ2VuY3kiLCJpYXQiOjE2MDY3NTgyMzIsImV4cCI6MTYwNjg0NDYzMiwiYXpwIjoiTE5mMFNQMGxkU3BOaUhLdVNRam94OHl4bFY1RmhMcVMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.BuTtjlExYo5FSDfdSSt9QY7fe7UiRSpDWWrytpt9d0M0ZZ7eoLeCBKx8LyulpoZBGjvOkDUKAM5XyU35hfZGW4N3kwfrbalqb8d_l-vjoxkaeSdEal50feqGAIQaT0hQWGceZEdwdqshcNQ3AEMiRMeEyEJOMa3sjIquOSOfLADVop7Mosa_uUErb_j9MvHqd6u1xv_PoDsgnPt8TVy5JhrB_QZOe-D3ECyGLdb5aQteV9JEp2HI49_UfP4JVlpvYDZR3oTkO8dkXzaxpkaPKj2e6F0bwopnFdgQy2UzKZfWbw4ZPII7pKFpAhnv9wIE0Y_uUZHcICYijYCmngXv2Q'
EXECUTIVE_PRODUCER_TOKEN = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImV1N0FSUGxQUVZDRlRpYlFGUkllSSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYWhtZWQtYWxzdWRhaXJpLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmM1MmEzNGIzMjhjOTAwNjk1N2FhODMiLCJhdWQiOiJjYXN0aW5nIF9hZ2VuY3kiLCJpYXQiOjE2MDY3NjA0MzcsImV4cCI6MTYwNjg0NjgzNywiYXpwIjoiTE5mMFNQMGxkU3BOaUhLdVNRam94OHl4bFY1RmhMcVMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.lymVXXbRrNArAYHlR7kpfLqjivKTF8GP_l-38dZ2n6ZgXiXmjn7oujGIXA2pVpdLIYiS8hxZjWwmbW-9Jl4pIbplwI08mpTW9NKSKM3TVWHuPa5Q-tQiTTBuPFqqDlW6N3N_p-8bF8oYCQbDUJ8R30WxxNBY31SMOJrHddhwUuyPFYp7L-1MLf9kOCKA87r1XDNi552Fnx9IL2iIFsb0YFNNWiTyd51JSWckN6qhFhW4mxbRWEO_jaV9QLNEkmxKkxqSbdlnTf5Qi-avvgq_VRO6uXodGbCzThBbH66pTIxYPvkyMsQbdsN7DmZkx9Dr_bPEkJzAMVOmANif4tmZaQ'
CASTING_DIRECTOR_TOKEN = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImV1N0FSUGxQUVZDRlRpYlFGUkllSSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYWhtZWQtYWxzdWRhaXJpLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmM1MmE0Y2QxZjM2ZTAwNzY3ZWE3OTIiLCJhdWQiOiJjYXN0aW5nIF9hZ2VuY3kiLCJpYXQiOjE2MDY3NjExMDAsImV4cCI6MTYwNjg0NzUwMCwiYXpwIjoiTE5mMFNQMGxkU3BOaUhLdVNRam94OHl4bFY1RmhMcVMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBvc3Q6bW92aWVzIl19.uSRaJXHvIjuG3Ot_VkTDrhNKpEVRIjBz9kLmq43jTqHhCac0cXP1ewTvNdohY95iFBb7zf19QnWuXljDs1z07DqQpxVuEOSwekSRd2cCjVK_YVk7DbyWFzAiI0iUr2iommiEyIor3xQixUofewg3sJgKfF2hKUMEet--8j6CCrNOrvdg1V-6OjEDRXb0QimBtujHVDWkTcW0Ev0iMtgWyoQeWcVQBZYlpRh3lCvjBRMskJW7ctHT6eHn0b8xdO6FIxlCeUEUDQZmI0qyHf176LYf8ljlyBZnDBHZGEjYBeIfjrtW3u4l_ZvsTz318UvKHQ-H2Atn7d_AdiDNWA_lRQ'


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
        response = self.client().get('/actors',
                                     headers={"Authorization": f"{CASTING_ASSISTANCE_TOKEN}"})
        print(response.data)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_get_actors_error(self):
        response = self.client().get('/actors?page=500',
                                     headers={"Authorization": f"{CASTING_ASSISTANCE_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], "Not Found")

    def test_get_movies(self):
        response = self.client().get('/movies',
                                     headers={"Authorization": f"{CASTING_ASSISTANCE_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_get_movies_error(self):
        response = self.client().get('/movies?page=500',
                                     headers={"Authorization": f"{CASTING_ASSISTANCE_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], "Not Found")

    def test_delete_actor(self):
        response = self.client().delete('/actors/1',
                                        headers={"Authorization": f"{CASTING_DIRECTOR_TOKEN}"})
        data = json.loads(response.data)

        actor = Actor.query.get(1)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 1)
        self.assertTrue(data['total_actors'])
        self.assertEqual(actor, None)

    def test_delete_actor_error(self):
        response = self.client().delete('/actors/1000',
                                        headers={"Authorization": f"{CASTING_DIRECTOR_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], "Not Found")

    def test_delete_movie(self):
        response = self.client().delete('/movies/1',
                                        headers={"Authorization": f"{EXECUTIVE_PRODUCER_TOKEN}"})
        data = json.loads(response.data)

        movie = Actor.query.get(1)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 1)
        self.assertTrue(data['total_movies'])
        self.assertEqual(movie, None)

    def test_delete_movie_error(self):
        response = self.client().delete('/movies/1000',
                                        headers={"Authorization": f"{EXECUTIVE_PRODUCER_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], "Not Found")

    def test_post_actor(self):
        response = self.client().post(
            '/actors',
            json={
                'name': 'Ahmed',
                'age': 22,
                'gender': 'male'},
            headers={
                "Authorization": f"{CASTING_DIRECTOR_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_actors'])

    def test_post_actor_error(self):
        response = self.client().post(
            '/actors',
            json={
                'firstName': 'Ahmed',
                'age': 22,
                'gender': 'male'},
            headers={
                "Authorization": f"{CASTING_DIRECTOR_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], "Bad Request")

    def test_post_movie(self):
        response = self.client().post(
            '/movies',
            json={
                'title': 'Toy Story',
                'release_date': '2020-12-12'},
            headers={
                "Authorization": f"{EXECUTIVE_PRODUCER_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_movies'])

    def test_post_movie_error(self):
        response = self.client().post(
            '/movies',
            json={
                'movieTitle': 'Toy Story',
                'release_date': '2020-12-12'},
            headers={
                "Authorization": f"{EXECUTIVE_PRODUCER_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], "Bad Request")

    def test_patch_actor(self):
        response = self.client().patch(
            '/actors/1',
            json={
                'name': 'Saleh',
                'age': 45,
                'gender': 'male'},
            headers={
                "Authorization": f"{CASTING_DIRECTOR_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_patch_actor_error(self):
        response = self.client().patch(
            '/actors/1',
            json={
                'firstName': 'Saleh',
                'age': 45,
                'gender': 'male'},
            headers={
                "Authorization": f"{CASTING_DIRECTOR_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], "Bad Request")

    def test_patch_movie(self):
        response = self.client().patch(
            '/movies/1',
            json={
                'title': 'Toy Story',
                'release_date': '2020-12-12'},
            headers={
                "Authorization": f"{CASTING_DIRECTOR_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_patch_movie_error(self):
        response = self.client().patch(
            '/movies/1',
            json={
                'movieTitle': 'Toy Story',
                'release_date': '2020-12-12'},
            headers={
                "Authorization": f"{CASTING_DIRECTOR_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], "Bad Request")

    def test_casting_assistant(self):
        response = self.client().get('/actors',
                                     headers={"Authorization": f"{CASTING_ASSISTANCE_TOKEN}"})
        print(response.data)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_casting_assistant_error(self):
        response = self.client().post(
            '/movies',
            json={
                'title': 'Toy Story',
                'release_date': '2020-12-12'},
            headers={
                "Authorization": f"{CASTING_ASSISTANCE_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], "Unauthorized")

    def test_casting_director(self):
        response = self.client().post(
            '/actors',
            json={
                'name': 'Ahmed',
                'age': 22,
                'gender': 'male'},
            headers={
                "Authorization": f"{CASTING_DIRECTOR_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_actors'])

    def test_casting_director_error(self):
        response = self.client().post(
            '/movies',
            json={
                'title': 'Toy Story',
                'release_date': '2020-12-12'},
            headers={
                "Authorization": f"{CASTING_DIRECTOR_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], "Unauthorized")

    def test_executive_producer(self):
        response = self.client().post(
            '/movies',
            json={
                'title': 'Toy Story',
                'release_date': '2020-12-12'},
            headers={
                "Authorization": f"{EXECUTIVE_PRODUCER_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_movies'])

    def test_executive_producer_error(self):
        response = self.client().post(
            '/actors',
            json={
                'name': 'Ahmed',
                'age': 22,
                'gender': 'male'},
            headers={
                "Authorization": f"{EXECUTIVE_PRODUCER_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], "Unauthorized")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
