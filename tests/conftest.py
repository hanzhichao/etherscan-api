import pytest

from etherscan_api.etherscan_api import get_etherscan_api


@pytest.fixture(scope='session')
def usdt():
    return '0x58c885900f2df7a1fb1cc1ec35dea9a1c786cac0'


@pytest.fixture(scope='session')
def account():
    return '0x3f217aF5b4d5Dc6467598937119E500ab758623a'


@pytest.fixture(scope='session')
def etherscan():
    return get_etherscan_api('eth', 'testnet')


@pytest.fixture(scope='session')
def block_no(etherscan):
    return int('0x91bc7a', 16)


@pytest.fixture(scope='session')
def block_timestamp(etherscan):
    return int('0x69088308', 16)


@pytest.fixture(scope='session')
def tx_hash():
    return '0x6c9afcd508388ea18a130f2764e7b45a7a2c402f7f31e3519795523192b237f8'
