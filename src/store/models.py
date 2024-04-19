from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Permission
from django.db import models


# Create your models here.


class Profile(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)


class CustomUser(AbstractUser):
    role_choices = [
        ('V', 'Vendeur'),
        ('GS', 'Gestionnaire de Stock'),
        ('A', 'Admin'),
    ]
    role = models.CharField(max_length=2, choices=role_choices)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='user_profile')
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='custom_users',  # Modification du related_name
        related_query_name='custom_user',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='custom_users_permissions',  # Modification du related_name
        related_query_name='custom_user_permission',
    )


class Gestionnaire(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Vous pouvez même ajouter d'autres champs spécifiques au gestionnaire ici


class Vendeur(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Ajoutez d'autres champs spécifiques au vendeur ici si nécessaire


class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Ajoutez d'autres champs spécifiques à l'administrateur ici si nécessaire
