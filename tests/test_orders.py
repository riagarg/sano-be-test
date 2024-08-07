import json
from core.models import User
from unittest.mock import Mock, patch

class TestOrders:
    def test_order_placement(self, test_client, data, mock_requests_post):
        user = User.get(name="Jane Doe")
        url = f"/users/{user.id}/dnakitorders"
        response = test_client.post(url, data={"sequencing_type": "sequence type 1", "shipping_info": "1 main st"})

        # print(mock_requests_post.call_args_list)
        mock_requests_post.assert_called_once_with("https://portal.dev.sanogenetics.com/dev/home-test/email-delivery-service",
                                                   data={'email': 'jane@gmail.com', 'text': 'Your order has been placed!'}, 
                                                   headers={'Content-Type': 'application/json', 'Authorization': 'Bearer 7lPIazekwQu7Raz7FqBQmsLvlH29IDwG'})
        assert response.status_code == 200
      
        data = json.loads(response.data)
        print(data)
        assert data['shipping_info'] == '1 main st'
        assert data['sequencing_type'] == 'sequence type 1'
        assert User.get(id=data['user']) == user
    
    def test_text_order_placement(self, test_client) :
        # TODO: Test an order placement with a different sequencing type
        pass
    
    def test_notification_service(self, test_client) :
        # TODO: Test that the notification service is calling the API and sending the correct inputs to notif service 
        pass