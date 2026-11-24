from typing import Protocol

import httpx_retry


class Storage(Protocol):
    def read(self, key: str) -> str: ...


class FileStorage:
    def read(self, key):
        return open(key).read()


def load(client, key):
    retry = httpx_retry.Retry(times=3)
    return retry.run(lambda: client.mget_many([key]))
