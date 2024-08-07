from flask import Blueprint, jsonify
from core.schemas import UserSchema, DNAKitOrderSchema
from core.models import User, DNAKitOrder
from playhouse.shortcuts import model_to_dict
import requests
from flask import request
from flask import abort
users_api = Blueprint("users_api", __name__)


@users_api.route("/users", methods=["GET"])
def get_all_users():
    users = User.select().prefetch(DNAKitOrder)
    for user in users:
        user_dict = model_to_dict(user)
        user_dict['orders'] = [model_to_dict(order) for order in user.orders]

    user_schema = UserSchema(many=True)
    return jsonify(user_schema.dump(users))

@users_api.route("/users/<user_id>/dnakitorders", methods=["POST"])
def post_order(user_id):
    try : 
        user = User.get(id=user_id) 
    except User.DoesNotExist: 
        abort(404)
        
    sequencing_type = request.form["sequencing_type"]
    shipping_info = request.form["shipping_info"] # shipping info could also come from the user address?

    order = DNAKitOrder.create(sequencing_type=sequencing_type, user=user, shipping_info=shipping_info)
    order.save()
    schema = DNAKitOrderSchema()
    order2 = DNAKitOrder.get(id=order.id)
    # print(order2.__dict__)
    result = schema.dump(order2)
    
    channel = "sms" if sequencing_type == "whole-exome-sequencing" else "email"
    notification_service = NotificationService()
    notification_service.notify(user=user, message="Your order has been placed!", channel=channel)

    return result


class NotificationService:
    def __init__(self):
        self.url = {
            "sms" : "https://portal.dev.sanogenetics.com/dev/home-test/sms-delivery-service",
            "email" : "https://portal.dev.sanogenetics.com/dev/home-test/email-delivery-service"
        }
        # This should go in environment variables not hard coded!!
        self.auth = {
            "sms":  "o8deGqg2vTGYXtvIsA05zOW8ywAPBQuB",
            "email": "7lPIazekwQu7Raz7FqBQmsLvlH29IDwG"
        }
    
    def notify(self, user, message, channel) :
        url = self.url[channel]
        auth = self.auth[channel]
        phone_payload = { "phone_number": user.phone_number, "text": message}
        email_payload = {"email": user.email, "text" : message}
        payload = phone_payload if channel == "sms" else email_payload
        
        try :
            response = requests.post(url, 
            data=payload,
            headers={"Content-Type": "application/json", "Authorization": "Bearer " + auth},
            )
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None
        #include some feedback to admin that notification service worked
        



