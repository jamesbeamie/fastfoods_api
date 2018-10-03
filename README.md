## FAST_FOOD_FAST
[![Build Status](https://travis-ci.org/jamesbeamie/fastfoods_api.svg?branch=develop)](https://travis-ci.org/jamesbeamie/fastfoods_api) [![Coverage Status](https://coveralls.io/repos/github/jamesbeamie/fastfoods_api/badge.svg?branch=develop)](https://coveralls.io/github/jamesbeamie/fastfoods_api?branch=develop)
 - An application interface for the fast food application.
 - This API has end points that allows the user to place a new order for food,
 - get a list of orders, get a specific order and update order status and delete the order.

## GETTING STARTED
- Set up a virtual environment for your application using pip install virtualenv command.
- Pip install all the dependencies for your application.
- Activate the virtual environment usin venv/Scripts/activate
- Clone the repository and run the application in your activated virtual environment.

## INSTALLING REQUIREMENTS
- You need Flask, pylint and pytest installed.
     - Flask: pip install Flask a micro-framework
     - Pylint: pip install pylint for pep8 linting
     - Pytest: pip install pytest for running tests

### How to run the application locally: 
- change directory on your terminal to the virtual environment
- change directory to the Scripts folder run < activate to activate the virtual environment >
- change directory to the root folder and run < python run.py > to run the application

## RUNNING TESTS
- Get to the terminal and run tests using pytest.
   - pytest -v
- Run test ccoverage for the code using travis.
   - Specify path to test file
   - pytest --cov=app/tests

### TESTING ON POSTMAN

- Clone the repo (https://github.com/jamesbeamie/fastfoodfastapi.git).
    ##### View all orders :Get to postman, select GET method and send the request using the url - http://127.0.0.1:8080/api/v1/orders
   ##### View a specific order : On postman, select GET method, add an id to the url - http://127.0.0.1:8080/api/v1/orders/1
    ##### Place an order :On postman, select POST method, add the input fields and send the request using the url -      http://127.0.0.1:8080/api/v1/orders
    ##### Update an order : On postman, select PUT method, add the input fields in the body section and send the request - http://127.0.0.1:8080/api/v1/orders/1
   ##### Delete an order : On postman, select DELETE method and add the id of the field to delete after the url - http://127.0.0.1:8080/api/v1/orders/1
   
## DEPLOYMENT
- Deployment to Heroku
    - signup for heroku
    - Heroku login
    - Install gunicorn
    - Push changes
    - Deploy
 
   


