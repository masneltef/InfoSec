import random

# Global variables to store user inputs
client_versions = []
server_versions = []
client_cipher_suites = []
server_cipher_suites = []

def main_menu():
    while True:
        print("\n--- TLS Handshake Simulation ---")
        print("1. Set TLS versions")
        print("2. Set cipher suites")
        print("3. Perform handshake")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            set_tls_versions()
        elif choice == '2':
            set_cipher_suites()
        elif choice == '3':
            perform_handshake()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def set_tls_versions():
    global client_versions, server_versions
    print("\n--- Set TLS Versions ---")
    print("Available TLS versions: TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3")
    
    client_versions = input("Enter client supported versions (comma-separated): ").split(',')
    client_versions = [v.strip().upper() for v in client_versions]
    
    server_versions = input("Enter server supported versions (comma-separated): ").split(',')
    server_versions = [v.strip().upper() for v in server_versions]
    
    print(f"Client versions set: {', '.join(client_versions)}")
    print(f"Server versions set: {', '.join(server_versions)}")

def set_cipher_suites():
    global client_cipher_suites, server_cipher_suites
    print("\n--- Set Cipher Suites ---")
    print("Available cipher suites: AES-128-GCM, AES-256-GCM, CHACHA20-POLY1305")
    
    client_cipher_suites = input("Enter client supported cipher suites (comma-separated): ").split(',')
    client_cipher_suites = [c.strip().upper() for c in client_cipher_suites]
    
    server_cipher_suites = input("Enter server supported cipher suites (comma-separated): ").split(',')
    server_cipher_suites = [c.strip().upper() for c in server_cipher_suites]
    
    print(f"Client cipher suites set: {', '.join(client_cipher_suites)}")
    print(f"Server cipher suites set: {', '.join(server_cipher_suites)}")

def perform_handshake():
    print("\n--- Performing TLS Handshake ---")
    
    if not client_versions or not server_versions:
        print("Error: TLS versions not set. Please set TLS versions first.")
        return
    
    if not client_cipher_suites or not server_cipher_suites:
        print("Error: Cipher suites not set. Please set cipher suites first.")
        return
    
    try:
        # Step 1: Version Negotiation
        negotiated_version = negotiate_version(client_versions, server_versions)
        print(f"Negotiated TLS Version: {negotiated_version}")
        
        # Step 2: Cipher Suite Selection
        selected_cipher_suite = select_cipher_suite(client_cipher_suites, server_cipher_suites)
        print(f"Selected Cipher Suite: {selected_cipher_suite}")
        
        # Step 3: Key Exchange
        shared_secret = diffie_hellman_exchange()
        print(f"Established Shared Secret: {shared_secret}")
        
        print("\nHandshake completed successfully!")
    
    except ValueError as e:
        print(f"Handshake failed: {str(e)}")

def negotiate_version(client_versions, server_versions):
    common_versions = set(client_versions) & set(server_versions)
    if not common_versions:
        raise ValueError("No common TLS version found")
    
    version_priority = ['TLS 1.3', 'TLS 1.2', 'TLS 1.1', 'TLS 1.0']
    for version in version_priority:
        if version in common_versions:
            return version
    
    raise ValueError("No valid TLS version found")

def select_cipher_suite(client_suites, server_suites):
    common_suites = set(client_suites) & set(server_suites)
    if not common_suites:
        raise ValueError("No common cipher suite found")
    
    suite_priority = ['AES-256-GCM', 'CHACHA20-POLY1305', 'AES-128-GCM']
    for suite in suite_priority:
        if suite in common_suites:
            return suite
    
    raise ValueError("No valid cipher suite found")

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
    
    # These should be equal
    if client_shared_secret == server_shared_secret:
        return client_shared_secret
    else:
        raise ValueError("Key exchange failed")

if __name__ == "__main__":
    main_menu()