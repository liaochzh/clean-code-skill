class FileStorage:
    def read(self, key):
        return open(key).read()


def load(client, key):
    return client.mget_many([key])
