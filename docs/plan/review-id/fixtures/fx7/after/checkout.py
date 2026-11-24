"""结账：汇总购物车并应用折扣。"""


def total(items):
    subtotal = sum(i["price"] * i["qty"] for i in items)
    return subtotal * 0.9
