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

    def check_token(self):
        try:
            self.key = self.jwks_client.get_signing_key(self.token).key
        except jwt.exceptions.PyJWKClientError as error:
            return {"status": "error", "msg": error.__str__()}
        except jwt.exceptions.DecodeError as error:
            return {"status": "error", "msg": error.__str__()}

        try:
            payload = jwt.decode(
                self.token,
                self.key,
                algorithms=self.config.algorithms,
                audience=self.config.api_uri,
                issuer=self.config.issuer,
            )
        except Exception as error:
            return {"status": "error", "msg": error.__str__()}
        if self.scopes:
            result = self._check_claims(payload, 'scope', str, self.scopes.split(' '))
            if result.get("error"):
                return result
        
        if self.permissions:
            result = self._check_claims(payload, 'permissions', list, self.permissions.split(' '))
            if result.get("error"):
                return result
        return result
        

    def claims_check(self, payload, cl_type, cl_name):
        if cl_name not in payload or not isinstance(payload[cl_name], cl_type):
            return {"status": "error", "msg": "Invalid authorization. No claim found in payload."}
        if cl_name == "scopes":
            payload_cl = payload[cl_name].split(" ")
        for e in excepted_val:
            if e not in payload_cl:
                return {"status": "error", "msg": "Invalid authorization. No claim found in payload."}
        return {"status": "success", "status_code": 200}
