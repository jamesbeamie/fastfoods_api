## FAST_FOOD_FAST
An application interface for the fast food front end.

## END POINTS FOR ORDERS PAGE

 ### DESCRIPTION
 - This API has end points that allows the user to place a new order for food,
 - get a list of orders, get a specific order and update order status.

### How to run the application locally: 
- change directory on your terminal to the virtual environment
- change directory to the Scripts folder run < activate to activate the virtual environment >
- change directory to the root folder and run < python run.py > to run the application
 

### TESTING ON POSTMAN

- Clone the repo (https://github.com/jamesbeamie/fastfoodfastapi.git).
    ##### View all orders : GET route - http://127.0.0.1:8080/api/v1/orders
   ##### Voew a specific order : GET route - http://127.0.0.1:8080/api/v1/orders/1
    ##### Place an order : POST route - http://127.0.0.1:8080/api/v1/orders
    ##### Update an order : PUT route - http://127.0.0.1:8080/api/v1/orders/1
   ##### Delete an order : the DELETE route - http://127.0.0.1:8080/api/v1/orders/1
   
### travisCI tests
[![Build Status](https://travis-ci.org/jamesbeamie/fastfoods_api.svg?branch=ft-delete-order-160325634)](https://travis-ci.org/jamesbeamie/fastfoods_api)
[![Coverage Status](https://coveralls.io/repos/github/jamesbeamie/fastfoods_api/badge.svg?branch=develop)](https://coveralls.io/github/jamesbeamie/fastfoods_api?branch=develop)
