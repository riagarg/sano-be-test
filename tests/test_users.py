import json 

class TestUsers:
    def test_get_all_users_api(self, test_client, data):

        response = test_client.get("/users")
        assert response.status_code == 200

        data = json.loads(response.data)
       
        #check number of users
        assert len(data) == 2  
        print(data)

        #check Jane Doe and associated orders
        assert data[0]['name'] == 'Jane Doe'
        assert data[0]['email'] == 'jane@gmail.com'
        assert len(data[0]['orders']) == 1
        assert data[0]['orders'][0]['sequencing_type'] == "whole-exome-sequencing"
        assert data[0]['orders'][0]['shipping_info'] == "1 main st"

        assert data[1]['name'] == 'John Doe'
        assert data[1]['email'] == 'john@gmail.com'
        assert len(data[1]['orders']) == 2
        assert data[1]['orders'][0]['sequencing_type'] == "another-type"
        assert data[1]['orders'][0]['shipping_info'] == "1 main st"
        assert data[1]['orders'][1]['sequencing_type'] == "another-type"
        assert data[1]['orders'][1]['shipping_info'] == "1 main st"

    def test_get_all_users_api(self, test_client, data):
        # test if the DB is empty 
        pass
        

