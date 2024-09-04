import random

def diffie_hellman_exchange():
    # This is a simplified version and should not be used in real-world applications
    prime = 23  # A small prime for demonstration
    base = 5    # A primitive root modulo prime
    
    # Client generates a private key and calculates public key
    client_private = random.randint(1, prime - 1)
    client_public = pow(base, client_private, prime)
    
    # Server generates a private key and calculates public key
    server_private = random.randint(1, prime - 1)
    server_public = pow(base, server_private, prime)
    
    # Both parties compute the shared secret
    client_shared_secret = pow(server_public, client_private, prime)
    server_shared_secret = pow(client_public, server_private, prime)
    
    # In a correct implementation, these should be equal
    if client_shared_secret == server_shared_secret:
        return client_shared_secret
    else:
        raise ValueError("Key exchange failed")