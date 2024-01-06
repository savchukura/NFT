import random

from data.data import Person
from faker import Faker
import os
faker_en = Faker()
Faker.seed()


def generated_person():
    yield Person(
        firstname=faker_en.first_name(),
        lastname=faker_en.last_name()
    )
