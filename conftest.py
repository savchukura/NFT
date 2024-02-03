import pytest
import requests
import json
from datetime import datetime
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

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
    data = {
        'idToken': id_token.json()['idToken'],
        'fingerprint': 'd1c8f9185507f41eef029f10f2fd939acc2d4a61',
    }
    headers = {"Content-Type": "application/json"}

    get_token = json.loads(
        requests.post(url="https://liquid-acre.zpoken.dev/api/v1/auth", json=data, headers=headers).text)

    token = get_token['accessToken']['access_token']
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


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()



