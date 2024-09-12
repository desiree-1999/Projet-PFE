from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class PersonManager(BaseUserManager):
    def create_user(self, email, nom, prenom, mot_de_passe=None):
        if not email:
            raise ValueError('L\'utilisateur doit avoir une adresse e-mail valide.')
        user = self.model(
            email=self.normalize_email(email),
            nom=nom,
            prenom=prenom,
            # role=role
        )
        user.set_password(mot_de_passe)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nom, prenom, mot_de_passe):
        user = self.create_user(
            email=self.normalize_email(email),
            nom=nom,
            prenom=prenom,
            mot_de_passe=mot_de_passe,
            #role='super_admin', 
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Person(AbstractBaseUser):
    ROLES = [('admin', 'administrateur'), ('user', 'utilisateur'), ('super_admin', 'super administrateur')]
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True)
    role = models.CharField(choices = ROLES,  default = 'user' )
    
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)

    EMAIL_FIELD = 'email'  # Utilisez l'email pour la connexion au lieu du username
    USERNAME_FIELD = 'username'  # Désactiver 'username' pour utiliser uniquement l'email
    # REQUIRED_FIELDS = ['nom', 'prenom']



    objects = PersonManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'prenom']

    def _str_(self):
        return f"{self.nom} {self.prenom}"
