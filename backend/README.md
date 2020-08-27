# Backend - Python + Flask + SQLAlchemy
## Stack

## Project Structure
### Setup
Setup the project by running `pipenv install`. This should install any packages needed

Harry has some issues, it was a bit picky
    I had to add the alternatives for python->python3 and pip->pip3

### Start
`pipenv run python -m flask run`
Visit http://localhost/api for the home api
Visit http://localhost/apidocs for the swagger documentation
### Run Tests
`pipenv run python -m unittest`


### To Enable hot reload
Add a file `./.env` with the following lines

FLASK_APP=app.py
FLASK_ENV=development

Then run the code as normal