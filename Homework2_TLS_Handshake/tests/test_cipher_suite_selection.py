
import unittest
from src.tls_handshake.cipher_suite_selection import select_cipher_suite

class TestCipherSuiteSelection(unittest.TestCase):
    def test_common_suite(self):
        client_suites = ['AES-128-GCM', 'AES-256-GCM']
        server_suites = ['AES-256-GCM', 'CHACHA20-POLY1305']
        self.assertEqual(select_cipher_suite(client_suites, server_suites), 'AES-256-GCM')

    def test_no_common_suite(self):
        client_suites = ['AES-128-GCM']
        server_suites = ['CHACHA20-POLY1305']
        with self.assertRaises(ValueError):
            select_cipher_suite(client_suites, server_suites)

    def test_most_secure_suite(self):
        client_suites = ['AES-128-GCM', 'AES-256-GCM', 'CHACHA20-POLY1305']
        server_suites = ['AES-128-GCM', 'AES-256-GCM', 'CHACHA20-POLY1305']
        self.assertEqual(select_cipher_suite(client_suites, server_suites), 'AES-256-GCM')