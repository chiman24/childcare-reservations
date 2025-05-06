# secrets_manager.py
import boto3
import json

# Module-level cache dictionary
_secret_cache = {}

def get_secret(secret_name: str, region_name: str = "us-east-1"):
    if secret_name in _secret_cache:
        return _secret_cache[secret_name]

    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region_name)

    response = client.get_secret_value(SecretId=secret_name)
    secret = response.get('SecretString')
    parsed = json.loads(secret)

    # Cache it
    _secret_cache[secret_name] = parsed

    return parsed
