import pytest
from brownie import Contract


def test_v1_swap(user, ausdt, get_ausdt, yv_empire):
    amount = 10_000 * 10 ** 6
    get_ausdt(user, amount)
    ausdt.approve(yv_empire, amount, {"from": user})
    yv_empire.migrate([(1, ausdt)], {"from": user})
    vault = Contract("0x7Da96a3891Add058AdA2E826306D812C638D87a7")
    assert vault.balanceOf(user) != 0


def test_v2_swap(user, ausdcv2, get_ausdcv2, yv_empire):
    amount = 10_000 * 10 ** 6
    get_ausdcv2(user, amount)
    ausdcv2.approve(yv_empire, amount, {"from": user})
    yv_empire.migrate([(2, ausdcv2)], {"from": user})
    vault = Contract("0x5f18C75AbDAe578b483E5F43f12a39cF75b973a9")
    assert vault.balanceOf(user) != 0
