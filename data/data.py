from dataclasses import dataclass

BASE_URL = "https://liquid-acre.zpoken.dev/"

BASE_USER = {'email': 'yura+e@zpoken.io', 'password': '213456qaZ'}


@dataclass
class Person:
    firstname: str = None
    lastname: str = None
    email: str = None
