import unittest
from homework_api import get_api
from nose.tools import assert_true
import requests


class TestApi(unittest.TestCase):
    def testApi(self):
        self.assertEqual(get_api.get_info_api('yalilu'), 'Right')
        self.assertEqual(get_api.get_info_api('mhassany'), 'Right')


#    def test_request_response(self):
#        # Send a request to the API server and store the response.
#        response = requests.get('http://jsonplaceholder.typicode.com/todos')
#
#        # Confirm that the request-response cycle completed successfully.
#        assert_true(response.ok)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(verbosity=2)
