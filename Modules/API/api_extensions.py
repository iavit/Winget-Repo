import os

from slowapi import Limiter
from slowapi.util import get_remote_address


api_limiter = Limiter(
    key_func=get_remote_address,
    storage_uri=os.getenv("SLOWAPI_LIMITER_STORAGE_URI", os.getenv("FLASK_LIMITER_STORAGE_URI", "memory://"))
)
