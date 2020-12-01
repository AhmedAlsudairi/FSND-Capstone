import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie

CASTING_ASSISTANCE_TOKEN = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImV1N0FSUGxQUVZDRlRpYlFGUkllSSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYWhtZWQtYWxzdWRhaXJpLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmM1MmEwNTYxZjllNzAwNzY4OTdmNzciLCJhdWQiOiJjYXN0aW5nIF9hZ2VuY3kiLCJpYXQiOjE2MDY4NDg2ODUsImV4cCI6MTYwNjkzNTA4NSwiYXpwIjoiTE5mMFNQMGxkU3BOaUhLdVNRam94OHl4bFY1RmhMcVMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.lffBxvuYUBFa7dRGd-HnoIqCNwBgUQZyRf8tIT4Tz_dx_uESF2NyaIaiPu-4NngVB_qvYzN_2JigX8hLxHRYjWaRfdHJObBL0c2DlJVWyNF0Grvpovs4EFgIsuvj_9R_1F_6GZToXbIWyksnaf5StO3Xf_cRCu5t-bk6dPxh-us1D2Ox4ebueBKlKLF2KXVtVT8xqwkdJUgyQz6UZmLUDcBDK1lTLVE85q6xxUKNet8FIIHudwktyUKxZ5L7fAzBtbHY7J-JDG5P-syVFUvR0sKd7Em37sH-Xxt-FudYICSr6KZh0j3skOXroxhtHxA6MqgXkPeIAlkfDSxo_27QTg'
CASTING_DIRECTOR_TOKEN = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImV1N0FSUGxQUVZDRlRpYlFGUkllSSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYWhtZWQtYWxzdWRhaXJpLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmM1MmEzNGIzMjhjOTAwNjk1N2FhODMiLCJhdWQiOiJjYXN0aW5nIF9hZ2VuY3kiLCJpYXQiOjE2MDY4NDkyODgsImV4cCI6MTYwNjkzNTY4OCwiYXpwIjoiTE5mMFNQMGxkU3BOaUhLdVNRam94OHl4bFY1RmhMcVMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.nR_QMzTOr80fXFFAaqtjxR912-WHFqzuMAPKikXps5HGZqCd2SpyHsbh9SYpLED_hVTjOdA9Prf-2D7VBk0194O69ShFalNh-8-ZbToYYq7wLhWgWmdcplndvbWwkzXmaI5DThk1Yn05Es47AxPQfnzNPiSBoqGwY3XHTfhCso41byByYcNR4fOGxuXyQSTeSTdxLkjJTMMoBUGyfOgMPVZdLPsOJ7DwSDnACV_1CIZGWXCmeBS9l9GdCWb6U3Lwa4v4CKbXyHzdlO_ryfdBVvlGIpwFoe5XFY9ssNgE7IfVxpnYTHw2s7jiOhg_cOd8MAv4wEk1Z-zej-bulKZuVg'
EXECUTIVE_PRODUCER_TOKEN = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImV1N0FSUGxQUVZDRlRpYlFGUkllSSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYWhtZWQtYWxzdWRhaXJpLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmM1MmE0Y2QxZjM2ZTAwNzY3ZWE3OTIiLCJhdWQiOiJjYXN0aW5nIF9hZ2VuY3kiLCJpYXQiOjE2MDY4NTU2MzksImV4cCI6MTYwNjk0MjAzOSwiYXpwIjoiTE5mMFNQMGxkU3BOaUhLdVNRam94OHl4bFY1RmhMcVMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.2lR3Yv6whNJcP5rUjrXjcZ05rIKSfosS1bMOMiB61oBXw9ROWbQ5X54hnrIWx-YBQQZ_hHwMdpPKbA2Q6mBigtADw3dvywhiJOnWzmgri6cfHcHISkKhEngvw5czi1j_u7GhJAvOScWw_DaU3D9sQ5QL66R1dcRmJcPLfnsURLWWHze_RWQ86BKHQ92eeHYdRW0thK3ENBx0qWZQK-dLXYDi9J4L03nPxRgZQPR4zuwK88c-Njdv1hMbsKhXdwPrdT8AXtRJZmP3FldF1Nmd_k_ZGQ_BaWFKmHPyHCX1xdsHCdIkeyitCx8Hm090EUc7aFn_lg7H-bvp_DaHCjxItQ'


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

    def second_test_executive_producer(self):
        response = self.client().post(
            '/actors',
            json={
                'name': 'Ahmed',
                'age': 22,
                'gender': 'male'},
            headers={
                "Authorization": f"{EXECUTIVE_PRODUCER_TOKEN}"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_actors'])
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
