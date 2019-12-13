from unittest.mock import Mock, MagicMock, patch
import requests
import unittest


def is_authentic_user(username, password):
    response = requests.get(
        'http://kudoo.com/api/user/is_authentic_user?username={0}&password={1}'.format(username, password))
    if response.status_code == 200:
        return True
    return False


class TestAuthenticUser(unittest.TestCase):

    def test_is_authentic_user(self):
        with patch('requests.get') as mocked_test:
            mocked_test.return_value.status_code = 200

            result = is_authentic_user('joy', '123$$')
            mocked_test.assert_called_with('http://kudoo.com/api/user/is_authentic_user?username=joy&password=123$$')
            self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
