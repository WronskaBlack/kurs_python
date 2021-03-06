import unittest
from unittest import mock
from parameterized import parameterized

from testowanie_TDD.functions_unittest import is_even, Account, Person, remove_file, is_correct_website


class BasicTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    def setUp(self) -> None:
        print('setUp')

    def tearDown(self) -> None:
        print('tearDown')

    @parameterized.expand([
        [20],
        [30],
        [10],
    ])
    def test_is_even(self, value):
        # Given
        # When
        result = is_even(value)
        # Then
        self.assertEqual(True, result, 'Hello')

    def test_is_odd(self):
        print('odd')
        result = is_even(21)
        self.assertEqual(False, result)

    @mock.patch('os.remove')
    def test_remove_file(self, os_mock):
        remove_file('incorect.txt')
        os_mock.assert_called()
        os_mock.assert_called_with('incorect.txt')

class Account_Card_Test(unittest.TestCase):
    def setUp(self) -> None:
        # Given
        self.test_account = Account('Jan', 'Kowalski', 6000003000)


    def test_account_owner(self):
        # When
        #self.test_account.owner = mock.MagicMock(return_value = 'Kazimierz')
        result = self.test_account.owner()
        # Then
        self.assertEqual('Jan Kowalski', result)

    def test_account_balance(self):
        # When
        result = self.test_account.balance()
        # Then
        self.assertEqual(0, result)

    def test_account_number(self):
        # When
        result = self.test_account.number()
        # Then
        self.assertEqual(6000003000, result)

    def test_account_transfer_positive(self):
        # When
        self.test_account.transfer(100)
        result = self.test_account.balance()
        # Then
        self.assertEqual(100, result)

    def test_account_transfer_negative(self):
        # When
        self.assertRaises(Exception, self.test_account.transfer, -1000)
        result = self.test_account.balance()
        # Then
        self.assertEqual(0, result)


class Person_Test(unittest.TestCase):
    def setUp(self) -> None:
        self.person = Person('Jan', 'Kowalski', 45)

    @parameterized.expand([
        ['doktor', 'doktor Jan Kowalski'],
        ['inżynier', 'inżynier Jan Kowalski'],
        ['magister', 'magister Jan Kowalski']
    ])
    def test_title(self, title, output):
        result = self.person.say_name_with_title(title)
        self.assertEqual(result, output)

class IsCorrectWebsiteTest(unittest.TestCase):
    @parameterized.expand([
        ['https://google.com', 200, True],
        ['https://wp.pl', 300, True],
        ['https://onet.pl', 400, False]
    ])
    def test_is_correct_with_200(self, url, status_code, expected):
        with mock.patch('requests.get') as requests_get_mock:
            requests_get_mock.return_value.status_code = status_code
            result = is_correct_website(url)
        self.assertEqual(expected, result)
