def negotiate_version(client_versions, server_versions):
    common_versions = set(client_versions) & set(server_versions)
    if not common_versions:
        raise ValueError("No common TLS version found")
    return max(common_versions)