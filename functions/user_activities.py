import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder

class UserData:

    def get_user_balance(self, token):
        headers = {
            "Authorization": f"Bearer {token}"
        }
        r = requests.get(url="https://liquid-acre.zpoken.dev/api/v1/store/wallet/balance", headers=headers)
        usdc_balance = r.json()['balance']['USDC']
        return usdc_balance

    def top_up_usdc_balance(self, token, amount):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        data = {
            'amount': amount
        }
        top_up = requests.post(url="https://liquid-acre.zpoken.dev/api/v1/store/wallet/top_up", json=data, headers=headers)
        return top_up.status_code

    def get_notifications(self, token):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        notifications = requests.get(url="https://liquid-acre.zpoken.dev/api/v1/notifications?page_size=3&page_number=1", headers=headers)
        print(notifications.json())

    def get_user_data(self, token):
        headers = {
            "Authorization": f"Bearer {token}"
        }
        r = requests.get(url="https://liquid-acre.zpoken.dev/api/v1/users/me", headers=headers)
        user_first_name = r.json()['user']['first_name']
        user_last_name = r.json()['user']['last_name']
        return user_first_name, user_last_name

    def edit_user_info(self, token, email, first_name, last_name, country):
        headers = {
            "Authorization": f"Bearer {token}"
        }
        data = {"data": f"""
            {{
                "email": "{email}",
                "first_name": "{first_name}",
                "last_name": "{last_name}",
                "country": "{country}"
            }}
        """}
        edit = json.loads(requests.put(url="https://liquid-acre.zpoken.dev/api/v1/users/me", data=data, headers=headers).text)
        return edit


