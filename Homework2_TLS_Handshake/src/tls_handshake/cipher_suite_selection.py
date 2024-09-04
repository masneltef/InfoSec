def select_cipher_suite(client_suites, server_suites):
    common_suites = set(client_suites) & set(server_suites)
    if not common_suites:
        raise ValueError("No common cipher suite found")
    return max(common_suites, key=cipher_suite_strength)

def cipher_suite_strength(suite):
    # Define strength order of cipher suites
    strength_order = ['AES-256-GCM', 'CHACHA20-POLY1305', 'AES-128-GCM']
    return -strength_order.index(suite) if suite in strength_order else float('-inf')