import jwt
import bcrypt

from src.core import settings


def encode_jwt(
    payload: dict,
    private_key: str = settings.AUTH.PRIVATE_KEY.read_text(),
    algorithm: str = settings.AUTH.ALGORITHM,
):
    encoded = jwt.encode(
        payload=payload,
        key=private_key,
        algorithm=algorithm,
    )
    return encoded


def decode_jwt(
    token: str | bytes,
    public_key: str = settings.AUTH.PUBLIC_KEY.read_text(),
    algorithm: str = settings.AUTH.ALGORITHM,
):
    decoded = jwt.decode(
        token=token,
        public_key=public_key,
        algorithm=[algorithm],
    )
    return decoded


def hash_password(
    password: str,
) -> bytes:
    salt = bcrypt.gensalt()
    pwd_bytes: bytes = password.encode()
    return bcrypt.hashpw(pwd_bytes, salt)


def validate_password(
    password: str,
    hashed_password: bytes,
) -> bool:
    return bcrypt.checkpw(
        password=password.encode(),
        hashed_password=hashed_password,
    )
