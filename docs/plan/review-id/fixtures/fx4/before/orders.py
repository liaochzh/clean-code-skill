class OrderService:
    def __init__(self, repo):
        self.repo = repo

    def total(self, user_id):
        return sum(o.amount for o in self.repo.by_user(user_id))
