from unittest.mock import Mock
import unittest
from unittest import TestCase
from mock import Mock, patch
from url_caller import UrlCaller
import requests
from requests.exceptions import Timeout
from requests import Response


#Should inherit TestCase
class TestUrlCaller(TestCase):

    @patch("url_caller.requests")
    @patch("url_caller.Response")
    def test_url_response(self, mocked_response, mocked_requests):
        mocked_requests.get.return_value = mocked_response
        mocked_response.status_code = 201
        url_caller = UrlCaller()
        status = url_caller.request("http://www.google.com")
        assert status == 201

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