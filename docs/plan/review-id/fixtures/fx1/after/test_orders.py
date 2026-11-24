from orders import total


def test_total():
    assert total([{"price": 10, "qty": 11}]) > 0
