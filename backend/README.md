# Backend - Python + Flask + SQLAlchemy

## Development
Install all dependencies for the project by running `pipenv install`.

### Start
`pipenv run python -m flask run`
Visit http://localhost/api for the home api
Visit http://localhost/apidocs for the swagger documentation

### Populate Database
`pipenv run python -m flask populate`

will populate the database with users, entries and messages. 
See `app.py` for specifics.

### Run Tests
`pipenv run python -m unittest`


### Hot Reload
Start the flask server with the following environment variables

```
FLASK_APP=app.py
FLASK_ENV=development
```

You can either
- Add a file `./.env` with the contents as above, or
- Prepend the command with the env vars `NAME=VALUE python -m flask run` like so