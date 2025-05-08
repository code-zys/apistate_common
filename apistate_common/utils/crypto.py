from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import json
import base64

class CredentialEncryption:
    def __init__(self, cert_path: str = 'app/assets/certificate/public_key.pem'):
        self.cert_path = cert_path
        self._load_public_key()
        self._load_private_key()
    
    def _load_public_key(self):
        with open(self.cert_path, 'rb') as key_file:
            self.public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )
    
    def _load_private_key(self):
        with open('app/assets/certificate/private_key.pem', 'rb') as key_file: #TODO: set filename as environment variable
            self.private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )
    
    def decrypt_credentials(self, encrypted_credentials: str) -> dict:
        """Decrypt credential options using the private key.
        
        Args:
            encrypted_credentials: Base64 encoded encrypted credentials
            
        Returns:
            dict: Decrypted credential options
        """
        # Decode base64 encrypted data
        encrypted = base64.b64decode(encrypted_credentials)
        
        # Decrypt using private key
        decrypted = self.private_key.decrypt(
            encrypted,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        # Parse JSON string back to dictionary
        return json.loads(decrypted.decode('utf-8'))
    
    def encrypt_credentials(self, credentials: dict) -> str:
        """Encrypt credential options using the public key certificate.
        
        Args:
            credentials: Dictionary containing credential options
            
        Returns:
            str: Base64 encoded encrypted credentials
        """
        # Convert credentials to JSON string
        credentials_bytes = json.dumps(credentials).encode('utf-8')
        
        # Encrypt using public key
        encrypted = self.public_key.encrypt(
            credentials_bytes,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        # Return base64 encoded encrypted data
        return base64.b64encode(encrypted).decode('utf-8')