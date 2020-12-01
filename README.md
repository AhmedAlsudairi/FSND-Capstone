# FSND-Capstone
FSND-Capstone is the final project of Udacity's Full Stack Web Developer Nanodegree.

## Motivation
This project aims to cover all concepts that we study in this nanodegree program, so it is a great opportunity to review all the concepts by practicing this project.


## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 


## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` directs flask to find the flask application. 


## API Documention

### Introduction

This API provide 8 endpoints for casting agency website. The endpoints cover all basic opearations on the database, get, delete, post, and update on actors and movies of the casting agency. 

### Base URL

This API is hosted in https://fsnd-capstone-ahmed.herokuapp.com/ .

### Roles:
1. Casting Assistant:
Can view actors and movies

2. Casting Director:
All permissions a Casting Assistant has and…
Add or delete an actor from the database
Modify actors or movies

3. Executive Producer:
All permissions a Casting Director has and…
Add or delete a movie from the database

### Roles Tokens (Authintication):
1. Casting Assistant: ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImV1N0FSUGxQUVZDRlRpYlFGUkllSSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYWhtZWQtYWxzdWRhaXJpLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmM1MmEwNTYxZjllNzAwNzY4OTdmNzciLCJhdWQiOiJjYXN0aW5nIF9hZ2VuY3kiLCJpYXQiOjE2MDY4NDg2ODUsImV4cCI6MTYwNjkzNTA4NSwiYXpwIjoiTE5mMFNQMGxkU3BOaUhLdVNRam94OHl4bFY1RmhMcVMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.lffBxvuYUBFa7dRGd-HnoIqCNwBgUQZyRf8tIT4Tz_dx_uESF2NyaIaiPu-4NngVB_qvYzN_2JigX8hLxHRYjWaRfdHJObBL0c2DlJVWyNF0Grvpovs4EFgIsuvj_9R_1F_6GZToXbIWyksnaf5StO3Xf_cRCu5t-bk6dPxh-us1D2Ox4ebueBKlKLF2KXVtVT8xqwkdJUgyQz6UZmLUDcBDK1lTLVE85q6xxUKNet8FIIHudwktyUKxZ5L7fAzBtbHY7J-JDG5P-syVFUvR0sKd7Em37sH-Xxt-FudYICSr6KZh0j3skOXroxhtHxA6MqgXkPeIAlkfDSxo_27QTg```

2. Casting Director:
```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImV1N0FSUGxQUVZDRlRpYlFGUkllSSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYWhtZWQtYWxzdWRhaXJpLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmM1MmEzNGIzMjhjOTAwNjk1N2FhODMiLCJhdWQiOiJjYXN0aW5nIF9hZ2VuY3kiLCJpYXQiOjE2MDY4NDkyODgsImV4cCI6MTYwNjkzNTY4OCwiYXpwIjoiTE5mMFNQMGxkU3BOaUhLdVNRam94OHl4bFY1RmhMcVMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.nR_QMzTOr80fXFFAaqtjxR912-WHFqzuMAPKikXps5HGZqCd2SpyHsbh9SYpLED_hVTjOdA9Prf-2D7VBk0194O69ShFalNh-8-ZbToYYq7wLhWgWmdcplndvbWwkzXmaI5DThk1Yn05Es47AxPQfnzNPiSBoqGwY3XHTfhCso41byByYcNR4fOGxuXyQSTeSTdxLkjJTMMoBUGyfOgMPVZdLPsOJ7DwSDnACV_1CIZGWXCmeBS9l9GdCWb6U3Lwa4v4CKbXyHzdlO_ryfdBVvlGIpwFoe5XFY9ssNgE7IfVxpnYTHw2s7jiOhg_cOd8MAv4wEk1Z-zej-bulKZuVg```

3. Executive Producer:
```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImV1N0FSUGxQUVZDRlRpYlFGUkllSSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYWhtZWQtYWxzdWRhaXJpLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmM1MmE0Y2QxZjM2ZTAwNzY3ZWE3OTIiLCJhdWQiOiJjYXN0aW5nIF9hZ2VuY3kiLCJpYXQiOjE2MDY4NTU2MzksImV4cCI6MTYwNjk0MjAzOSwiYXpwIjoiTE5mMFNQMGxkU3BOaUhLdVNRam94OHl4bFY1RmhMcVMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.2lR3Yv6whNJcP5rUjrXjcZ05rIKSfosS1bMOMiB61oBXw9ROWbQ5X54hnrIWx-YBQQZ_hHwMdpPKbA2Q6mBigtADw3dvywhiJOnWzmgri6cfHcHISkKhEngvw5czi1j_u7GhJAvOScWw_DaU3D9sQ5QL66R1dcRmJcPLfnsURLWWHze_RWQ86BKHQ92eeHYdRW0thK3ENBx0qWZQK-dLXYDi9J4L03nPxRgZQPR4zuwK88c-Njdv1hMbsKhXdwPrdT8AXtRJZmP3FldF1Nmd_k_ZGQ_BaWFKmHPyHCX1xdsHCdIkeyitCx8Hm090EUc7aFn_lg7H-bvp_DaHCjxItQ```
### Error

1. Code: 422, Message: Unprocessable Entity,
Response: ```{
      "success" : False,
      "status_code" : 422,
      "message" : "Unprocessable Entity"
    }```
2. Code: 404, Message: Not Found,
Response: ```{
      "success" : False,
      "status_code" : 404,
      "message" : "Not Found"
    }```
3. Code: 400, Message: Bad Request,
Response: ```{
      "success" : False,
      "status_code" : 400,
      "message" : "Bad Request"
    }  ```
4. Code: 401, Message: Unauthorized,
Response: ```{
        "success": False,
        "error": 401,
        "message": "Unauthorized"
    }  ``` 
5. Code: 403, Message: Forbidden,
Response: ```{
        "success": False,
        "error": 403,
        "message": "Forbidden"
    }  ```      
6. Code: 405, Message: Method not allowed,
Response: ```{
        "success": False,
        "error": 405,
        "message": "Method not allowed"
    }  ```   

### Resourse endpoints    

1. Method: GET, URI: '/actors'  
-Description: This endpoint will retrieve all actors from the database.
-Requiered Role: Casting Assistant, or Casting Director, or Executive Producer. 
-Parameters: None
-Response: ```{
    "actors": [
        {
            "age": 25,
            "gender": "female",
            "id": 3,
            "name": "sara"
        },
        {
            "age": 22,
            "gender": "fmale",
            "id": 4,
            "name": "hamed"
        }
    ],
    "success": true
}```

2. Method: DELETE, URI: '/actors/<int:actor_id>'  
-Description: This endpoint will delete the actor with a given id.
-Requiered Role: Casting Director, or Executive Producer. 
-Parameters: None
Response: ```{
    "deleted": 4,
    "success": true,
    "total_actors": 1
}```

3. Method: POST, URI: '/actors'  
-Description: This endpoint will create a new actor with given parameters.
-Requiered Role: Casting Director, or Executive Producer. 
-Parameters: name, age, gender
Response: ```{
    "success": true,
    "created": 3,
    "total_actors": 3
}```

4. Method: PATCH, URI: '/actors/<int:actor_id>'  
-Description: This endpoint will update a existing actor with  given parameters.
-Requiered Role: Casting Director, or Executive Producer. 
-Parameters: name, age, gender
Response: ```{
    "actors": [
        {
            "age": 12,
            "gender": "male",
            "id": 3,
            "name": "ahmed"
        }
    ],
    "success": true
}```

5. Method: GET, URI: '/movies' 
-Description: This endpoint will retrieve all movies from the database.
-Requiered Role: Casting Assistant, or Casting Director, or Executive Producer. 
-Parameters: None
Response: ```{
    "movies": [
        {
            "release_date": "Sat, 12 Dec 2020 00:00:00 GMT",
            "title": "Toy Story"
        }
    ],
    "success": true
}```

6. Method: DELETE, URI: '/movies/<int:movie_id>'  
-Description: This endpoint will delete the movie with a given id.
-Requiered Role: Executive Producer. 
-Parameters: None
Response: ```{
    "success": true,
    "deleted": 2,
    "total_movies": 1
}```

7. Method: POST, URI: '/movies'  
-Description: This endpoint will create a new movie with given parameters.
-Requiered Role: Executive Producer. 
-Parameters: title, release_date
Response: ```{
    "success": true,
    "created": 3,
    "total_movies": 4
}```

8. Method: PATCH, URI: '/movies/<int:movie_id>'  
-Description: This endpoint will update a existing movie with  given parameters.
-Requiered Role: Casting Director, or Executive Producer. 
-Parameters: title, release_date
Response: ```{
    "movies": [
        {
            "release_date": "Sat, 12 Dec 2020 00:00:00 GMT",
            "title": "Toy Story"
        }
    ],
    "success": true
}```

## Testing
To run the tests, run
```
dropdb casting_agency_test
createdb casting_agency_test
python test_app.py
```
