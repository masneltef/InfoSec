import unittest
from src.tls_handshake.key_exchange import diffie_hellman_exchange

class TestKeyExchange(unittest.TestCase):
    def test_key_exchange(self):
        shared_secret = diffie_hellman_exchange()
        self.assertIsInstance(shared_secret, int)
        self.assertTrue(0 < shared_secret < 23)  # Based on the prime used in your implementation

    def test_multiple_exchanges(self):
        # Multiple exchanges should (usually) produce different results
        results = [diffie_hellman_exchange() for _ in range(10)]
        self.assertTrue(len(set(results)) > 1)  # At least some should be different

if __name__ == '__main__':
    unittest.main()