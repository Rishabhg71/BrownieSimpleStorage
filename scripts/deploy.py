from brownie import accounts, SimpleStorage, network

private_key = "<your_private_key>"


def deploy_contract(account):
    simple_storage = SimpleStorage.deploy({"from": account})
    val = simple_storage.retrieve()
    print(val)
    updated = simple_storage.store(200, {"from": account})
    val = simple_storage.retrieve()

    print(val)


def get_account():
    if network.show_active() == "developement":
        return accounts[0]
    else:
        return accounts.add(private_key)


def main():
    deploy_contract(get_account())
