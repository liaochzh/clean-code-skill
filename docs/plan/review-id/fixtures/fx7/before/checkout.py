"""结账：汇总购物车并应用折扣。"""
from discount import FixedDiscount


def total(items):
    subtotal = sum(i["price"] * i["qty"] for i in items)
    return FixedDiscount().apply(subtotal)
