import pytest
import requests
import json

# Define a fixture to set up the base URL for your API
@pytest.fixture
def base_url():
    return "https://liquid-acre.zpoken.dev/api/v1/"

# Define a fixture to perform any setup steps needed for your API tests
@pytest.fixture
def setup():
    # Perform setup steps, if any
    print("Setting up for API tests")
    yield  # This is where the test will run
    # Perform teardown steps, if any
    print("Tearing down after API tests")


# Define a fixture to create a sample authentication token
@pytest.fixture
def auth_token():
    data = {
        'email': 'yura@zpoken.io',
        'password': '213456qaZ',
        'returnSecureToken': True
    }
    id_token = requests.post(
        url='https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyDLejcXq2tpapC9Gk93O1aUv18LIM1xKRY',
        data=json.dumps(data))
    #print(id_token.json()['idToken'])
    data = {
        'idToken': id_token.json()['idToken'],
        'fingerprint': 'd1c8f9185507f41eef029f10f2fd939acc2d4a61',
    }
    headers = {"Content-Type": "application/json"}

    get_token = json.loads(
        requests.post(url="https://liquid-acre.zpoken.dev/api/v1/auth", json=data, headers=headers).text)

    token = get_token['accessToken']['access_token']
    #print(token)
    return token


# Define a fixture to make an API request
@pytest.fixture
def make_api_request(base_url, auth_token):
    def _make_api_request(endpoint, method='get', data=None, headers=None):
        url = f"{base_url}/{endpoint}"
        headers = headers or {}
        headers['Authorization'] = f"Bearer {auth_token}"

        data = {
            'amount': data
        }

        if method.lower() == 'get':
            response = requests.get(url, headers=headers)
        elif method.lower() == 'post':
            response = requests.post(url, json=data, headers=headers)
        elif method.lower() == 'put':
            response = requests.put(url, json=data, headers=headers)
        elif method.lower() == 'delete':
            response = requests.delete(url, headers=headers)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        return response

    return _make_api_request
#In your test functions, you can then use these fixtures:

#python
#Copy code
def test_api_functionality(setup, make_api_request):
    # Your test code here
    response = make_api_request('endpoint', method='get')
    assert response.status_code == 200
    # Add more assertions as needed