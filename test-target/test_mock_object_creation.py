from unittest.mock import Mock
import unittest
from unittest import TestCase

#Should inherit TestCase
class TestMockBuilder(TestCase):

    def test_create_mock(self):
        mocked = Mock()
        assert mocked is not None
        print("mocked object:{0}".format(mocked))


if __name__ == "__main__":
    print("test mock creation")
    unittest.main()

