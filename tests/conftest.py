import pytest
from app import create_app, create_tables
from core.models import User, DNAKitOrder
from unittest.mock import patch


@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        create_tables()
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!
        # drop_tables()

#Populate the db with sample data
@pytest.fixture(scope='module')
def data():
    user1 = User.create(name="Jane Doe", email="jane@gmail.com", phone_number="07451277972", password_hash="janepass", address="1 main st")
    user2 = User.create(name="John Doe", email="john@gmail.com", phone_number="07451277972", password_hash="johnpass", address="1 main st")
    order1 = DNAKitOrder.create(sequencing_type='whole-exome-sequencing', user=user1, shipping_info="1 main st")
    order2 = DNAKitOrder.create(sequencing_type='another-type', user=user2, shipping_info="1 main st")
    order3 = DNAKitOrder.create(sequencing_type='another-type', user=user2, shipping_info="1 main st")
    yield
    DNAKitOrder.delete().execute()
    User.delete().execute()

#Used to mock requests to external email/sms notif service 
@pytest.fixture
def mock_requests_post():
    with patch('requests.post') as mock_post:
        yield mock_post

    


