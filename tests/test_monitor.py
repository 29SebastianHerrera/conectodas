import pytest
import json
from models.trainer import Trainer
from models.user import User


@pytest.fixture
def trainer_json():
    with open('tests/Json/trainer.json') as content:
        trainer_json = json.load(content)
    return trainer_json


@pytest.fixture
def trainer():
    return Trainer(
        name='Sebastian',
        lastName='Herrera',
        age=21,
        phone=632432654,
        email='sebastianherrera@gmail.com'
    )


@pytest.fixture
def user_json():
    with open('tests/Json/user.json') as content:
        user_json = json.load(content)
    return user_json


@pytest.fixture
def user():
    return User(
        name='Cecilia',
        lastName='Contreras',
        age=70,
        phone=643567543,
        email='ceciliacontreras@gmail.com'
    )


def test_trainer_to_json_return_json(trainer, trainer_json):
    result = trainer.to_json()

    assert result == trainer_json


def test_user_to_json_return_json(user, user_json):
    result = user.to_json()

    assert result == user_json
