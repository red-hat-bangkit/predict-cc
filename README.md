# PREDICT BACKEND
A backend repository for PREDICT application

## Contribute to this repository
* See [contributing.md](contributing.md)

## Frontend Usage
* Go to [https://bangkit-predict.herokuapp.com/gql](https://bangkit-predict.herokuapp.com/gql)
* Try query bellow
<p align="center"><img src="docs/usage.png" width="700px"></p>

## Backend Usage
* Install requirements
    ```
    pip install -r requirements.txt
    ```

* Run application
    ```
    python main.py
    ```
    _go to http://localhost:8000/gql_

* Alembic migration (in future)
    ```
    alembic revision --autogenerate -m "Init Migration"

    alembic upgrade head
    ```

## Docker usage
* Build image
    ```
    docker build -t predictws:0.0.1 .
    ```
* Run container from image
    ```
    docker run --name predict_app -p 80:8080 predictws:0.0.1
    ```
* Stop and remove container
    ```
    docker container stop predict_app && docker rm $_
    ```

## Heroku deployment
* Connect repository to heroku app
    ```
    heroku git:remote -a <HEROKU-APP-NAME>
    ```
* Set heroku stack to container
    ```
    heroku stack:set container
    ```
* Deploy to heroku
    ```
    git push -f heroku master
    ```