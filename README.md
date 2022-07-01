![image](https://user-images.githubusercontent.com/13378850/176657886-e99a1dff-afcf-431f-a093-757cddba0d15.png)

# Sano Genetics Backend Engineer Test
Thank you for taking the time to work on the Sano Genetics Backend Engineer test!

⚠️ Please, create a **private** repository on GitHub and import this project.

Instead of commiting your changes directly to the main/master branch, create a separate branch to commit your changes to. At the end of the test, submit a pull request to the main/master branch. This will allow us to see all the changes during the code review.

Use as many commits as you normally would and write a detailed description for the PR to describe any decisions you've made and anything else you feel is relevant.

Ideally, you should aim to spend no longer than 3 hours on the tasks. If you can’t completely finish it, that’s not a problem - just explain what is left to do and how you would do it.

If, due to time constraints, you prefer to take some shortcuts, or in a real world scenario you would implement a particular logic/code in a better way, please feel free to leave comments thoughout your code explaining your alternative approach.


# Installation
This project was created using Python 3.8.10.

Install all dependencies, and run the application using:
```
export FLASK_ENV=development                                  
flask run
```


# Test tasks
The test consist of creating an endpoint to allow our admin users to place DNA Kit Orders for existing users.

1. Create an endpoint that allows admin staff to place DNA Kit Orders for existing users.

    1.1. placing an order should notify the user that the order was successfully placed. We also would like to be able to specify the notification channel (`email` or `sms`).
    
    DNAKitOrders of type `whole-exome-sequencing` should notify users via SMS while other types should notify them via email. See **Email/SMS Delivery API integrations** below.
    
    1.2 We have been considering the creation of a **NotificationService**. Our first draft of how developers would interact with it looks like this:
    ```python
    notification_service.notify(user, message="Your order has been placed!", channel='sms')
    ```
    But we are open to suggestions!
    We expect this service to be extended in the future (eg. add new channels like push notifications) with minimal changes to existing client code.


2. Update the existing `GET /users/` endpoint to return an additional `orders` property, containing all DNAKitOrders associated with each user.


3. Create tests for the above use cases. Notice that, the external delivery APIs should not be accessed during server tests, as their usage is limited to production only. **However, we do want to test the notification logic/code.**


## Email/SMS delivery API integrations
The goal here is to replicate a scenario where we need to integrate our application with an external service (like [Postmark](https://postmarkapp.com/), [Amazon SES](https://aws.amazon.com/ses/) or [Twilio](https://www.twilio.com/messaging)).
To make things easier, we have created two fake endpoints (they won't actually send emails nor SMSs) to mimic those external services:

### Email delivery API

> `POST https://dev.sanogenetics.com/dev/home-test/email-delivery-service`

API token is required on each request: `Authorization: Bearer <token>`

token = `7lPIazekwQu7Raz7FqBQmsLvlH29IDwG`

Expected payload example:
```json
{
    "recipient": "user@email.com",
    "message": "Hi {user_name}, your order has been successfully placed."
}
```

### SMS delivery API
> `POST https://dev.sanogenetics.com/dev/home-test/sms-delivery-service`

An API token is required on each request: `Authorization: Bearer <token>`

token = `o8deGqg2vTGYXtvIsA05zOW8ywAPBQuB`

Expected payload example:
```json
{
    "recipient": "07451277972",
    "message": "Hi {user_name}, your order has been successfully placed."
}
```

## Additional details
For context, here's some of the things we expect to assess in this test:
* Documentation and clarity
* Testing 
* Architecture & System design
* Web standards
* Error handling

Feel free to refactor the provided boilerplate code or update anything that you think doesn't look right or could be improved.


# Submitting the test
Please, give @sano-review access to the private repository and send us a link to the PR via email.

