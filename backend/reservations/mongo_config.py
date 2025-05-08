# mongo_config.py

import os

if os.environ.get("LOAD_MONGO_SECRET", "true").lower() == "true":
    from mongoengine import connect
    from .secrets_manager import get_secret

    secret = get_secret("dev/jv/mongodb")

    mongo_uri = (
        f"mongodb://{secret['username']}:{secret['password']}"
        f"@{secret['host']}:27017/?tls=true"
    )

    mongo_uri = f"mongodb://{secret['username']}:{secret['password']}@{secret['host']}:27017/?tls=true"

    print("🔌 Connecting to MongoDB...")

    connect(
        db=secret['database'],
        host=mongo_uri,
        alias="default"
    )
