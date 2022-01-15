from brownie import accounts, SimpleStorage


def test_deploy():
    account = accounts[0]
    simple_store = SimpleStorage.deploy({'from': account})
    starting = simple_store.retrieve()
    assert starting == 0
