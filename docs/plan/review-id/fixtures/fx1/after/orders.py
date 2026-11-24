def total(items):
    return sum(item["price"] * item["qty"] for item in items)


def proc(d, t):
    return [x * t for x in d]


def render(is_test=False):
    if is_test:
        return "test page"
    return "production page"
