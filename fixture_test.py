import pytest
import random


@pytest.fixture()                #декоратор для объявления функции как фикстуры
def create_user(open_browser):   #передали порядок и зависимость выполнения фикстур
    pass

def test_body(open_browser, create_user):
    assert open_browser == "browser"
    assert create_user == 25

def test_body2(open_browser, create_user):
    pass

def test_body3(open_browser, create_user):
    pass