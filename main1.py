from encryption_tools import encrypt_with_kms, decrypt_with_kms, generate_kms_key
from key_management import store_key_in_vault, retrieve_key_from_vault
from network_live_analysis import analyze_network_activity
from ssl_tls_security import create_ssl_server, create_ssl_client

key_id = generate_kms_key()
data = "Sensitive data that needs encryption"
encrypted_data = encrypt_with_kms(data, key_id)
decrypted_data = decrypt_with_kms(encrypted_data, key_id)
print(f"Decrypted Data: {decrypted_data}")

vault_url = "http://localhost:8200"
vault_token = "your-vault-token"
store_key_in_vault(data, vault_url, vault_token)
retrieved_key = retrieve_key_from_vault(vault_url, vault_token)
print(f"Retrieved Key from Vault: {retrieved_key}")

analyze_network_activity()

create_ssl_server('localhost', 12345, 'server.crt', 'server.key')
create_ssl_client('localhost', 12345, 'server.crt')
