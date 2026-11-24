"""折扣策略协议：为后续多策略做准备。"""
from typing import Protocol


class DiscountPolicy(Protocol):
    def apply(self, amount: float) -> float: ...
