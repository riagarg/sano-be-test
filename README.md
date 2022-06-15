# Sano Genetics Backend Engineer test
Thank you for taking the time to work of the Sano Genetics Backend Engineer test!

Please ensure that you have forked this project ensuring your forked repository is private. Please add your work to the fork and open a Pull request with your changes. Use the PR description to describe any decisions you've made and anything else you feel is relevant.

You should ideally aim to spend no longer than 3 hours on the tasks. If you can’t completely finish that’s not a problem - just explain what is left to do and how you would do it.

Please fork the repository ensuring your forked repository is private.

# Installation
This project was created using Python 3.8.10.

Install all dependencies, and run the application using:
```
export FLASK_ENV=development                                  
flask run
```


# Test tasks
The test consist of creating a backoffice endpoint to allow our admin users to place DNA Kit Orders on behalf of users.

1. Create an endpoint that allows admin staff to place DNA Kit Orders on behalf of users

    1.1. placing an order should notify the user that the order was successfully placed. 
    We also would like to be able to specify the notification type (`email` or `sms`). DNAKitOrders of type `whole-exome-sequencing` should notify users via SMS while other types should notify them via email. See **Email/SMS Delivery API integrations** below.

2. Update the existing `GET /users/` endpoint to return an additional `orders` property, containing all DNAKitOrders associated with each user.

3. Create tests for the above use cases. Notice that, the external delivery APIs should not be accessed during server tests, as its usage is limited to production only. However, we do want to test for the notification logic/code.

## Email/SMS Delivery API integrations
The goal here is to replicate a scenario where we need to integrate our application with an external service.
To make things simple, we've created two fake endpoints (they won't actually send emails nor SMSs) to mimic those external services:

**Email delivery API:**

> `POST https://dev.sanogenetics.com/dev/home-test/email-delivery-service`

API token is required on each request: `Authorization: Bearer <token>`

token = `7lPIazekwQu7Raz7FqBQmsLvlH29IDwG`

**SMS delivery API:**
> `POST https://dev.sanogenetics.com/dev/home-test/sms-delivery-service`

An API token is required on each request: `Authorization: Bearer <token>`

token = `o8deGqg2vTGYXtvIsA05zOW8ywAPBQuB`

Both services expect an object in the following format:
```json
{
    "recipient": "[email | phone]",
    "message": "Hi {user_name}, Your order has been successfully placed."
}
```


For context, here's some of the things we expect to assess in this test:
* **Documentation and clarity:** doc strings, variable names, type hints, comments, breaking into smaller functions, etc.
* **Testing:** unit tests, mocks, etc.
* **Architecture & System design:** patterns, packaging, etc.
* **Web API:** HTTP methods and status codes, REST principles, URL structure and encoding.
* **Error handling:** Exceptions, transaction rollbacks, etc.

Feel free to refactor the provided boilerplate code and update anything that you think doesn't look right or could be improved.

If due to time constraints you prefer to take some shortcuts or if you know that in a real world scenario you would implement a particular logic/code in a better way, please feel free to leave comments thoughout your code explaining your alternative approach.


# Submitting the test:
Please email the fork/PR to us and give the GitHub users: willgdjones,  jonathanmach and dsmurrell access to the forked private repository.

