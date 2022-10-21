from unittest import mock
from ocpp_auth_key.ocpp_auth_key import OcppAuthKey


class TestOcppAuthKey:

    def mocked_urandom(self):
        return b'\x13M\xd5\xb9\x89i\x16G\x1e6\xb3\xac\x99_\xd9?@\x82\xb81'

    @mock.patch('os.urandom', side_effect=mocked_urandom)
    def test_key(self, urandom_function):
        result = OcppAuthKey().bytes()
        assert result == b'\x13M\xd5\xb9\x89i\x16G\x1e6\xb3\xac\x99_\xd9?@\x82\xb81'
        assert len(result) == 20

    @mock.patch('os.urandom', side_effect=mocked_urandom)
    def test_b64_encoded(self, urandom_function):
        result = OcppAuthKey().b64_encoded()
        assert result == "E03VuYlpFkceNrOsmV/ZP0CCuDE="

    @mock.patch('os.urandom', side_effect=mocked_urandom)
    def test_hex(self, urandom_function):
        result = OcppAuthKey().hex()
        assert result == "134dd5b9896916471e36b3ac995fd93f4082b831"