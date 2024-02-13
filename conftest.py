import pytest
import random
#в этом файле pytest будет искать фикстуры и хуки

@pytest.fixture(scope="session")                #декоратор для объявления функции как фикстуры; scope="session" - фикстура выполнится только один раз на всю сессию
def open_browser():              #фикстуры выполняются либо перед тестом, либо после теста
    b = "browser"
    print("Браузер открыт.")
    print("Случайное число: ", random.randint(0, 100))
    return "username", "password"
    yield b                      #во время выполнения теста
    b = ""                       #выполнится после завершения теста
    print("Браузер закрыт!")     #выполнится после завершения теста

