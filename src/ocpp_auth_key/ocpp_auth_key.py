import os
from base64 import b64encode


class OcppAuthKey:

    def __init__(self, length=20):
        self.key = os.urandom(length)

    def bytes(self):
        return self.key

    def b64_encoded(self):
        return b64encode(self.key).decode("utf-8")

    def hex(self):
        return self.key.hex()