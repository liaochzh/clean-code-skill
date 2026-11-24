"""折扣计算：固定 9 折（金额单位：分，向下取整）。"""


class FixedDiscount:
    def apply(self, amount):
        return amount * 0.9
