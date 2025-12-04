from datetime import datetime, timedelta
from typing import Optional

from jose import jwt
from passlib.context import CryptContext

# TODO: move this to environment variables for real apps
SECRET_KEY = "change-this-secret-key-later"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def _normalize_password(password: str) -> str:
    """
    Make sure password is a string and not longer than 72 characters.
    Bcrypt only guarantees the first 72 bytes, so we safely truncate.
    """
    if password is None:
        raise ValueError("Password cannot be None")
    password = str(password)
    if len(password) > 72:
        password = password[:72]
    return password


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check a plain password against a stored hash."""
    normalized = _normalize_password(plain_password)
    return pwd_context.verify(normalized, hashed_password)


def get_password_hash(password: str) -> str:
    """Original name used in users.py (kept for compatibility)."""
    normalized = _normalize_password(password)
    return pwd_context.hash(normalized)


def hash_password(password: str) -> str:
    """Alias used by auth.py. Both do the same thing."""
    return get_password_hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Create a signed JWT access token."""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
