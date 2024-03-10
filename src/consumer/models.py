from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    email = models.EmailField(
        unique=True,
    )
    username = models.CharField(
        max_length=45,
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    # # Adicione related_name para evitar conflitos
    # groups = models.ManyToManyField(Group, related_name='user_groups')
    # user_permissions = models.ManyToManyField(Permission, related_name='user_permissions')

    def __str__(self):
        return self.username