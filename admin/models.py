from django.db import models
from hashlib import sha256


class Admin(models.Model):
    username = models.CharField(max_length=30)
    password_hash = models.CharField(max_length=64)

    def create(self, username, password):
        self.username = username
        self.password_hash = sha256(password.encode("utf-8")).hexdigest()
        self.save()
