## FAST_FOOD_FAST
An application interface for the fast food front end.

## END POINTS FOR ORDERS PAGE

 ### DESCRIPTION
 - This API has end points that allows the user to place a new order for food,
 - get a list of orders, get a specific order and update order status.

### The functions are to allow the user: 
- view all orders
 > #### pivortal tracker story
   - https://www.pivotaltracker.com/story/show/160309430
- view a specific order.
 > #### pivortal tracker story
   - https://www.pivotaltracker.com/story/show/160309461
- place an order.
 > #### pivortal tracker story
   - https://www.pivotaltracker.com/story/show/160309422
- update an order.
 > #### pivortal tracker story
   - https://www.pivotaltracker.com/story/show/160309503
- delete an order.
 > #### pivortal tracker story
   - https://www.pivotaltracker.com/story/show/160325634

### TESTING ON POSTMAN

- Clone the repo (https://github.com/jamesbeamie/fastfoodfastapi.git).
    ##### View all orders : GET route - http://127.0.0.1:8080/api/v1/orders
   ##### Voew a specific order : GET route - http://127.0.0.1:8080/api/v1/orders/1
    ##### Place an order : POST route - http://127.0.0.1:8080/api/v1/orders
    ##### Update an order : PUT route - http://127.0.0.1:8080/api/v1/orders/1
   ##### Delete an order : the DELETE route - http://127.0.0.1:8080/api/v1/orders/1
   
### travisCI tests
[![Build](https://travis-ci.org/jamesbeamie/fastfoods-api.svg?branch=master)](!:https://travis-ci.org/jamesbeamie/fastfoods-api)
[![Coverage Status](https://coveralls.io/repos/github/jamesbeamie/fastfoods-api/badge.svg?branch=master)](https://coveralls.io/github/jamesbeamie/fastfoods-api?branch=master)
