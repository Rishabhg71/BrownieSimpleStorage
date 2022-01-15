from os import read
from brownie import accounts, SimpleStorage, network


def read_contract():
    print(SimpleStorage[0].retrieve())


def main():
    read_contract()
