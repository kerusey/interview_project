
from .models import Admin
from hashlib import sha256


def check_if_admin_valid(login: str, password: str) -> bool:
    password_hash = sha256(password.encode("utf-8")).hexdigest()
    try:
        user = Admin.objects.get(username=login)
    except Exception: #TODO: find the name of exception
        return False
    return user.password_hash == password_hash
