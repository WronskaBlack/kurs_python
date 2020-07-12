import unittest
import pytest
from testowanie_TDD.functions_pytest import is_palindrom, count_even_odd, find_max3, Wallet
from testowanie_TDD.functions_unittest import Account


@pytest.mark.parametrize("value, result", [
    (1, 2),

])
def test_basic(value, result):
    assert 1 == 1


class BasicTestCase(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(1, 1)


@pytest.mark.parametrize('value, expected', [
    ('kajak', True),
    ('kot', False),
    ("leci bażant na żabi cel", True),
    ('Lisa Bonet ate no basil', True),
    ('Że też łże jeż? łże też!', True)
])
def test_is_palindrom(value, expected):
    result = is_palindrom(value)
    assert expected == result


@pytest.fixture()
def give_account():
    return Account("Kamil", "Nowak", 22233345)


def test_owner(give_account):
    result = give_account.owner()
    assert "Kamil Nowak" == result


def test_balance(give_account):
    result = give_account.balance()
    assert 0 == result


def test_transfer_positive(give_account):
    give_account.transfer(100)
    assert 100 == give_account.balance()


def test_transfer_negative(give_account):
    with pytest.raises(Exception):
        give_account.transfer(-1000)


@pytest.mark.parametrize('numbers, out', [
    ([1, 2, 5, 6, 73], {'count_even': 2, 'count_odd': 3}),
    ([1, 2, 5, 6, 0], {'count_even': 3, 'count_odd': 2})
])
def test_count_even_odd(numbers, out):
    result = count_even_odd(numbers)
    assert result == out


@pytest.mark.parametrize('numbers, expected', [
    ([1, 3, 3, 4], 36),
    ([4, 3, 3, 1], 36),
    ([4, -3, -3, 1], 36),
    ([-4, -3, -3, -1], -9)
])
def test_find_max3(numbers, expected):
    result = find_max3(numbers)
    assert result == expected


@pytest.fixture()
def new_wallet():
    return Wallet()


def test_balance_wallet(new_wallet):
    result = new_wallet.balance
    assert 0 == result


def test_add_cash(new_wallet):
    new_wallet.add_cash(100)
    result = new_wallet.balance
    assert 100 == result


def test_spend_cash_positive(new_wallet):
    new_wallet.add_cash(100)
    new_wallet.spend_cash(50)
    result = new_wallet.balance
    assert 50 == result


def test_spend_cash_negative(new_wallet):
    with pytest.raises(Exception):
        new_wallet.spend_cash(1000)