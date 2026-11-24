def summarize(rows):
    return sum(r["amount"] for r in rows)
