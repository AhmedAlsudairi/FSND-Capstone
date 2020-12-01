# FSND-Capstone
FSND-Capstone is the final project of Udacity's Full Stack Web Developer Nanodegree.
## API Documention

### Introduction

This API serve trivia react app which allow the user to browse through avaliable questions, search for question, filter questions by category, post new question, and play quiz for specific category.

### Getting started

This API is hosted in localhost https://fsnd-capstone-ahmed.herokuapp.com/ .

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
