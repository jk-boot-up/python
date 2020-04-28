from unittest import TestCase
import unittest

class TestWithPatches(TestCase):
    pass


if __name__ == "__main__":
    try:
        print("-----------------------------------------------")
        print("-----------------------------------------------")
        unittest.main()
    except BaseException as e:
        pass
    finally:
        print("completed main flow")
        print("-----------------------------------------------")
        print("-----------------------------------------------")
