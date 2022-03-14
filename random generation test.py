import os
import uuid
import secrets

stringling = str(uuid.uuid4().hex) + str(os.urandom(25)) + str(uuid.uuid4()) + str(secrets.token_urlsafe(16))
print(stringling)