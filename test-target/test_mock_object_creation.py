from unittest.mock import Mock
import unittest
from unittest import TestCase
import json


#Should inherit TestCase
class TestMockBuilder(TestCase):

    def test_create_mock(self):
        mocked = Mock()
        assert mocked is not None
        print("mocked object:{0}".format(mocked))

    def test_simple_class_loop_me(self):
        simple_class = SimpleClass()
        mock = Mock()
        assert simple_class.loop_me(mock)

    def test_json_mock(self):
        x = Mock()
        b = x
        b.loads('{"A1": "V1"}')
        b.loads.assert_called()
        b.loads.assert_called_with('{"A1": "V1"}')
        b.loads.assert_called_once_with('{"A1": "V1"}')
        print("json mock x is:{}".format(x))
        print("json mock ref b is:{}".format(b))


class SimpleClass:

    def loop_me(self, something):
        i = 0
        while i < 3:
            i = i+1
            print(something)
        return True


if __name__ == "__main__":
    try:
        print("test mock creation")
        unittest.main()
    except BaseException as e:
        pass
    finally:
        print("completed main flow")

