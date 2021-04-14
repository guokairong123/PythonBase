import pytest


def func(x):
    return x + 1


@pytest.mark.parametrize('a,b', [
    (1, 2),
    (2, 2)
])
def test_answer(a, b):
    assert func(a) == b


def test_answer1():
    assert func(4) == 5


@pytest.fixture()
def login():
    print("登录操作")
    usrname = 'Mike'
    return usrname


class TestDemo:
    def test_a(self, login):

        print(f'a  usrname = {login}')

    def test_b(self):
        print('b')


if __name__ == '__main__':
    pytest.main(['test_demo.py::TestDemo', '-v'])
