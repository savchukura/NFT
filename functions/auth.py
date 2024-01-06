import requests
import json

class Auth:

    def get_bearer(self, email, password):
        data = {
            'email': email,
            'password': password,
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
