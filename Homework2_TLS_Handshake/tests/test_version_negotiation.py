
import unittest
from src.tls_handshake.version_negotiation import negotiate_version

class TestVersionNegotiation(unittest.TestCase):
    def test_common_version(self):
        client_versions = ['TLS 1.2', 'TLS 1.3']
        server_versions = ['TLS 1.1', 'TLS 1.2', 'TLS 1.3']
        self.assertEqual(negotiate_version(client_versions, server_versions), 'TLS 1.3')

    def test_no_common_version(self):
        client_versions = ['TLS 1.0', 'TLS 1.1']
        server_versions = ['TLS 1.2', 'TLS 1.3']
        with self.assertRaises(ValueError):
            negotiate_version(client_versions, server_versions)

    def test_highest_common_version(self):
        client_versions = ['TLS 1.0', 'TLS 1.1', 'TLS 1.2']
        server_versions = ['TLS 1.1', 'TLS 1.2']
        self.assertEqual(negotiate_version(client_versions, server_versions), 'TLS 1.2')