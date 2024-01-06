import requests
import json
from functions.auth import Auth
from functions.user_activities import UserData
from pytest import mark
from generator.generator import generated_person

class TestUser:
    amount = [0.50, 500.00, 500.50]

    @mark.parametrize('amount', amount)
    def test_top_up(self, amount):
        auth = Auth()
        token = auth.get_bearer('yura@zpoken.io', '213456qaZ')
        balance = UserData()
        usdc_before = balance.get_user_balance(token)
        top_up = balance.top_up_usdc_balance(token, amount)
        usdc_after = balance.get_user_balance(token)
        assert top_up == 200
        assert float(usdc_after) == float(usdc_before) + float(amount)

    def test_get_user_balance(self, auth_token):
        balance = UserData()
        usdc_before = balance.get_user_balance(auth_token)
        print(usdc_before)

    def test_get_user_data(self, auth_token):
        user_data = UserData()
        user_first_name, user_last_name = user_data.get_user_data(auth_token)
        print(user_first_name, user_last_name)

    def test_edit_user_data(self, auth_token):
        person_info = next(generated_person())
        first_name = person_info.firstname
        last_name = person_info.lastname
        user_data = UserData()
        user_data.edit_user_info(auth_token, 'yura@zpoken.io', first_name, last_name, 'Ukraine')
        user_first_name, user_last_name = user_data.get_user_data(auth_token)
        assert user_first_name == first_name
        assert user_last_name == last_name


