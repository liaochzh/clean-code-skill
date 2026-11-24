def summarize(rows):
    return sum(r["amount"] for r in rows)


# def summarize(rows):
#     total = 0
#     for r in rows:
#         total += r["amount"]
#     return total


def summarize_debug(rows):
    print(rows)
    return summarize(rows)
