import requests
import json
from functions.auth import Auth
from functions.user_activities import UserData
from pytest import mark


def test_one(setup):
    data = {
        'email': 'yura@zpoken.io',
        'password': '213456qaZ',
        'returnSecureToken': True
    }
    response_one = requests.post(
        url='https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyBdIX1_ImQjOLlLEj6B7LfLHlo52mAZqiA',
        data=json.dumps(data))
    id_token = response_one.json()['idToken']
    print(id_token)


def test_get_bearer(setup):
    data = {
        'email': 'yura@zpoken.io',
        'password': '213456qaZ',
        'returnSecureToken': True
    }
    response_one = requests.post(
        url='https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyDLejcXq2tpapC9Gk93O1aUv18LIM1xKRY',
        data=json.dumps(data))
    id_token = response_one.json()['idToken']
    print(id_token)
    data = {
        'idToken': response_one.json()['idToken'],
        'fingerprint': 'd1c8f9185507f41eef029f10f2fd939acc2d4a61',
    }
    headers = {"Content-Type": "application/json"}

    res = json.loads(
        requests.post(url="https://liquid-acre.zpoken.dev/api/v1/auth", json=data, headers=headers).text)
    token = res['accessToken']['access_token']
    print(token)

def test_form_data(setup):
    data = {
        'email': 'yura@zpoken.io',
        'password': '213456qaZ',
        'returnSecureToken': True
    }
    response_one = requests.post(
        url='https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyDLejcXq2tpapC9Gk93O1aUv18LIM1xKRY',
        data=json.dumps(data))
    id_token = response_one.json()['idToken']
    data = {
        'idToken': response_one.json()['idToken'],
        'fingerprint': 'd1c8f9185507f41eef029f10f2fd939acc2d4a61',
    }
    headers = {"Content-Type": "application/json"}

    res = json.loads(
        requests.post(url="https://liquid-acre.zpoken.dev/api/v1/auth", json=data, headers=headers).text)
    token = res['accessToken']['access_token']
    headers = {
        "Authorization": f"Bearer {token}"
    }

    edit = json.loads(requests.put(url="https://liquid-acre.zpoken.dev/api/v1/users/me",
                                   data={"email": 'yura@zpoken.io', "first_name": 'test_name', "last_name": 'test_last',
                                         "country": 'Ukraine'}, headers=headers).text)

    print(edit)
class TestAuth:

    amount = [0.50, 500.00, 500.50]
    def test_three(self):
        auth = Auth()
        token = auth.get_bearer('yura@zpoken.io', '213456qaZ')
        balance = UserData()
        usdc_balance = balance.get_user_balance(token)
        print(usdc_balance)

    @mark.parametrize('amount', amount)
    def test_four(self, amount):
        auth = Auth()
        token = auth.get_bearer('yura@zpoken.io', '213456qaZ')
        balance = UserData()
        usdc_before = balance.get_user_balance(token)

        balance.top_up_usdc_balance(token, amount)
        usdc_after = balance.get_user_balance(token)
        assert float(usdc_after) == float(usdc_before) + float(amount)

    def test_five(self):
        amount = 0.50
        auth = Auth()
        token = auth.get_bearer('yura@zpoken.io', '213456qaZ')
        balance = UserData()
        usdc_before = balance.get_user_balance(token)

        balance.top_up_usdc_balance(token, amount)
        usdc_after = balance.get_user_balance(token)
        assert float(usdc_after) == float(usdc_before) + float(amount)

    def test_six(self):
        auth = Auth()
        token = auth.get_bearer('yura@zpoken.io', '213456qaZ')
        user_data = UserData()
        notification = user_data.get_notifications(token)
        #print(notification)

    def test_seven(self):
        amount = 100
        auth = Auth()
        token = auth.get_bearer('yura@zpoken.io', '213456qaZ')
        balance = UserData()

        top_up = balance.top_up_usdc_balance(token, amount)

        assert top_up == 200

    def test_nine(self, make_api_request):
        request = make_api_request('store/wallet/balance', 'get', None, None)
        print(request.json())

    def test_ten(self, make_api_request):
        request = make_api_request('store/wallet/top_up', 'post', 100, None)
        print(request.json())



