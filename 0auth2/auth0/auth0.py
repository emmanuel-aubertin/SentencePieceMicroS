import os
import jwt

class Config:
    domain: str
    api_uri: str
    issuer: str
    algorithms: str

def get_config():
    env = os.getenv("ENV", ".env")
    if env == ".env":
        config = Config()
        config.domain       = os.getenv('DOMAIN') or None
        config.api_uri      = os.getenv('API_URI') or None
        config.issuer       = os.getenv('ISSUER') or None
        config.algorithms   = os.getenv('ALGORITHMS') or None
        return config
    return None

class tokenValidator:
    def __init__(self, token, permissions=None, scopes=None):
        self.token = token
        self.permissions = permissions
        self.scopes = scopes
        self.config = get_config()
        self.jwks_client = self.PyJWKClient(f'https://{self.config.domain}/.well-known/jwks.json')




