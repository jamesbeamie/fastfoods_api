

## END POINTS FOR ORDERS AND FOODS PAGE
 ### DESCRIPTION
 - This API has end points that allows the user to place a new order for food,
 - get a list of orders, get a specific order and update order status and delete the order.

### How to run the application locally: 
- change directory on your terminal to the virtual environment
- change directory to the Scripts folder run < activate to activate the virtual environment >
- change directory to the root folder and run < python run.py > to run the application
 

### TESTING ON POSTMAN

- Clone the repo (https://github.com/jamesbeamie/fastfoodfastapi.git).
    ##### View all orders :Get to postman, select GET method and send the request using the url - http://127.0.0.1:8080/api/v1/orders
   ##### View a specific order : On postman, select GET method, add an id to the url - http://127.0.0.1:8080/api/v1/orders/1
    ##### Place an order :On postman, select POST method, add the input fields and send the request using the url - http://127.0.0.1:8080/api/v1/orders
    ##### Update an order : On postman, select PUT method, add the input fields in the body section and send the request - http://127.0.0.1:8080/api/v1/orders/1
   ##### Delete an order : On postman, select DELETE method and add the id of the field to delete after the url - http://127.0.0.1:8080/api/v1/orders/1

### ADDED AN END POINT TO RETURN ALL ORDERS
- This end point returns all orders
##### TravisCi badges
- [![Build Status](https://travis-ci.org/jamesbeamie/fastfoods_api.svg?branch=ft-all-orders-160309430)](https://travis-ci.org/jamesbeamie/fastfoods_api)
##### Coveralls
- [![Coverage Status](https://coveralls.io/repos/github/jamesbeamie/fastfoods_api/badge.svg?branch=develop)](https://coveralls.io/github/jamesbeamie/fastfoods_api?branch=develop)

### END POINT TO RETURN SPECIFIC ORDER
- This end point return returns a specific order specified by id
##### TravisCI test coverage
- [![Build Status](https://travis-ci.org/jamesbeamie/fastfoods_api.svg?branch=ft-return-specific-160309461)](https://travis-ci.org/jamesbeamie/fastfoods_api)
##### Coveralls Test coverag
- [![Coverage Status](https://coveralls.io/repos/github/jamesbeamie/fastfoods_api/badge.svg?branch=develop)](https://coveralls.io/github/jamesbeamie/fastfoods_api?branch=develop)

### END POINT TO PLACE AN ORDER
- This allows a user to place an order by providing order details
##### TravisCI coverage
- [![Build Status](https://travis-ci.org/jamesbeamie/fastfoods_api.svg?branch=ft-update-order-160309503)](https://travis-ci.org/jamesbeamie/fastfoods_api)
##### Coveralls
- [![Coverage Status](https://coveralls.io/repos/github/jamesbeamie/fastfoods_api/badge.svg?branch=develop)](https://coveralls.io/github/jamesbeamie/fastfoods_api?branch=develop)
### END POINT TO UPDATE AN ORDER
- This allows a user to update an order by providing order details
### END POINT TO DELETE AN ORDER
- This allows a user to delete an order by providing order details
##### TravisCI coverage
- [![Build Status](https://travis-ci.org/jamesbeamie/fastfoods_api.svg?branch=ft-delete-order-160325634)](https://travis-ci.org/jamesbeamie/fastfoods_api)
### TEST COVERAGE ON DEVELOP
##### travisCI tests
[![Build Status](https://travis-ci.org/jamesbeamie/fastfoods_api.svg?branch=develop)](https://travis-ci.org/jamesbeamie/fastfoods_api)
[![Coverage Status](https://coveralls.io/repos/github/jamesbeamie/fastfoods_api/badge.svg?branch=develop)](https://coveralls.io/github/jamesbeamie/fastfoods_api?branch=develop)


## ADDED A TEST FOR THE DELETE_ORDER END POINT
- This tests incase the url of the end point does not have an id supplied
## TravisCI coverage
- [![Build Status](https://travis-ci.org/jamesbeamie/fastfoods_api.svg?branch=ch-add-test-160742653)](https://travis-ci.org/jamesbeamie/fastfoods_api)
## Coveralls
- [![Coverage Status](https://coveralls.io/repos/github/jamesbeamie/fastfoods_api/badge.svg?branch=ft-all-food-160710916)](https://coveralls.io/github/jamesbeamie/fastfoods_api?branch=ft-all-food-160710916)

