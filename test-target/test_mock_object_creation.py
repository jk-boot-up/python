from unittest.mock import Mock
import unittest
from unittest import TestCase
import requests
from requests.exceptions import Timeout


#Should inherit TestCase
class TestMockBuilder(TestCase):

    def test_create_mock(self):
        print("**********************************")
        mocked = Mock()
        assert mocked is not None
        print("mocked object:{0}".format(mocked))
        print("**********************************")

    def test_mock_return_value(self):
        print("**********************************")
        mocked = Mock(return_value = "return value is True")
        print("return value mock:{}".format(mocked))
        print(mocked)
        print("**********************************")

    def test_mock_init_exception(self):
        print("**********************************")
        mocked = Mock(side_effect = Exception)
        print("Exception mock:{}".format(mocked))
        print("**********************************")
    def test_mock_init_name(self):
        print("**********************************")
        mocked = Mock(name = "mocked with name")
        print("named mock:{}".format(mocked))
        print("**********************************")

    def test_mock_configure(self):
        print("**********************************")
        mocked = Mock()
        mocked.configure_mock(return_value=False)
        print("configured mock:{}".format(mocked))
        print(mocked)
        print("**********************************")

    def test_simple_class_loop_me(self):
        print("**********************************")
        simple_class = SimpleClass()
        mock = Mock()
        assert simple_class.loop_me(mock)
        print("**********************************")

    def test_json_mock(self):
        print("**********************************")
        x = Mock()
        b = x
        result = b.loads('{"A1": "V1"}')
        print("json loads result is :{0}".format(result))
        b.loads.return_value = "Completed"
        result = b.loads('{"A1": "V1"}')
        print("json loads result is :{0}".format(result))
        b.loads.assert_called()
        b.loads.assert_called_with('{"A1": "V1"}')
        #b.loads.assert_called_once_with('{"A1": "V1"}')
        print("json mock x is:{}".format(x))
        print("json mock ref b is:{}".format(b))
        print("call count is:{}".format(b.loads.call_count))
        print("call args is:{}".format(b.loads.call_args))
        print("call args list is:{}".format(b.loads.call_args_list))
        print("method_calls is:{}".format(b.method_calls))
        print("**********************************")

    def test_json_return_value_with_mock(self):
        print("**********************************")
        mocked_json = Mock()
        print("mocked json return value:{0}".format(mocked_json.loads('{"A1": "V1"}')))
        mocked_json.loads.return_value = "{'result':'Completed'}"
        print("controlled return value is:{0}".format(mocked_json.loads("{a:b}")))
        assert mocked_json.loads("{a:b}") == "{'result':'Completed'}"
        print("**********************************")

    def test_request_for(self):
        print("**********************************")
        simple_class = SimpleClass()
        requests = Mock()
        requests.get.return_value = "response"
        result = simple_class.requests_for("https://google.com")
        print("requests result is:{0}".format(result))
        print("**********************************")



class SimpleClass:

    def loop_me(self, something):
        i = 0
        while i < 3:
            i = i+1
            print(something)
        return True

    def requests_for(self, url):
        r = requests.get(url)
        if r.status_code == 200:
            return r
        return None

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


