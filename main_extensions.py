import os

from flask_seasurf import SeaSurf
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


csrf = SeaSurf()

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=[],
    storage_uri=os.getenv("FLASK_LIMITER_STORAGE_URI", "memory://")
)
