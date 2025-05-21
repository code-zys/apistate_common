from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as symmetric_padding
from cryptography.hazmat.backends import default_backend
import json
import base64
import os

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
        """Encrypt credential options using hybrid encryption (AES + RSA).
        
        Args:
            credentials: Dictionary containing credential options
            
        Returns:
            str: Base64 encoded encrypted credentials
        """
        # Generate a random AES key
        aes_key = os.urandom(32)  # 256-bit key
        iv = os.urandom(16)  # 128-bit IV
        
        # Convert credentials to JSON string
        credentials_bytes = json.dumps(credentials).encode('utf-8')
        
        # Pad the data
        padder = symmetric_padding.PKCS7(128).padder()
        padded_data = padder.update(credentials_bytes) + padder.finalize()
        
        # Encrypt data with AES
        cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        
        # Encrypt the AES key with RSA
        encrypted_key = self.public_key.encrypt(
            aes_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        # Combine everything into a single structure
        combined = {
            'key': base64.b64encode(encrypted_key).decode('utf-8'),
            'iv': base64.b64encode(iv).decode('utf-8'),
            'data': base64.b64encode(encrypted_data).decode('utf-8')
        }
        
        # Return base64 encoded combined data
        return base64.b64encode(json.dumps(combined).encode('utf-8')).decode('utf-8')
    
    def decrypt_credentials(self, encrypted_credentials: str) -> dict:
        """Decrypt credential options using hybrid decryption (AES + RSA).
        
        Args:
            encrypted_credentials: Base64 encoded encrypted credentials
            
        Returns:
            dict: Decrypted credential options
        """
        # Decode the combined structure
        combined = json.loads(base64.b64decode(encrypted_credentials).decode('utf-8'))
        
        # Decode components
        encrypted_key = base64.b64decode(combined['key'])
        iv = base64.b64decode(combined['iv'])
        encrypted_data = base64.b64decode(combined['data'])
        
        # Decrypt the AES key using RSA
        aes_key = self.private_key.decrypt(
            encrypted_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        # Decrypt the data using AES
        cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
        
        # Remove padding
        unpadder = symmetric_padding.PKCS7(128).unpadder()
        data = unpadder.update(padded_data) + unpadder.finalize()
        
        # Parse JSON string back to dictionary
        return json.loads(data.decode('utf-8'))