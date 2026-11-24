class OrderService:
    def __init__(self, repo):
        self.repo = repo

    def total(self, user_id):
        return sum(o.amount for o in self.repo.by_user(user_id))

    def handle(self, user_id, kind, amount):
        if kind == "refund" and amount > 0 and not self.repo.locked(user_id):
            return self.repo.refund(user_id, amount)
        return self.repo.charge(user_id, amount)

    def export_invoice(self, user_id):
        return {"user_id": user_id, "lines": [], "status": "ok"}


def parse_user_agent(ua):
    return ua.split("/")[0]
