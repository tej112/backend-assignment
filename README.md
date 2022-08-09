# Backend-Assingment

## Setup and Run the Server

To run the server, run the following command:
  
  ```python main:app```
  or
  ```python main:app --reload```for auto-reload.
  or 
  ```python main:app --host=localhost --port=8080``` for custom host and port.
  or 
  ```python main:app --host=localhost --port=8080 --reload``` for custom host and port with auto-reload.

  If python is not recognized, you can use replace ```python``` with ```python3``` command

  example:
  ```python3 main:app```

  ## Usage
  The folllowing end points are available:

  - `/`:
    -`GET`:
      - Root endpoint. Returns ```{"message": "Hello World"}```

  - `/api/users?page=<page>&limit=<limit>&sort=<sort>&name=<name>`:
    -`GET`:
      - Returns users filtered by the given parameters.

  - `/api/users/`:
    -`POST`:
      - Creates a new user.
      - Returns `{}` if the user was created successfully with status sode of `201`.
      - if user with the given id already exists, returns `{"detail":"user already exists"}` with status code of `400`.

  - `/api/users/<id>/`:
    -`GET`:
      - Returns the user with the given id.
      - If no user with the given id exists, returns `{"detail":"uuser not found"}` with status code of `404`.

  - `/api/users/<id>/`:
    -`PUT`:
      - Updates the user with the given id.
      - Only the given fields are updated. And remaining fields are not updated.
      - If no user with the given id exists, returns `{"detail":"user not found"}` with status code of `404`.
      - Returns `{}` if the user was updated successfully with status sode of `200`.
  
  - `/api/users/<id>/`:
    -`DELETE`:
      - Deletes the user with the given id.
      - If no user with the given id exists, returns `{"detail":"user not found"}` with status code of `404`.
      - Returns `{}` if the user was deleted successfully with status sode of `200`.

  - `/populateDB`:
    -`POST`:
      - Populates the database with the given sample users.
      - Returns `{"message": "Successfully populated database"}` if the database was populated successfully with status sode of `200`.

  - `/docs`:
    -`GET`:
      - Returns the documentation in markdown format.
      - Swagger documentation is used for Documention and examples for input data models are given for `POST`,`PUT` endpoints for creating and updating users.

## Deployment
  
  # DataBase Used: 
  - For the sake of simplicity DataBase used is SQLite.
  - This API can be connected to any SQL DataBase using URL and Password if we want to use it with SQL Server(POSTGRES, MySQL, etc.,)

  # Heroku Deployment
  - The same server is deployed to Heroku Service.
  - `https://`
  - Here the DataBase is empty and if you want to use the end points you can POST a request to this URL which will populate the server so that you can use different endpoints.
