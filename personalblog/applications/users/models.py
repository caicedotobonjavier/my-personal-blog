from django.db import models
#
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Correo Electronico', max_length=254, unique=True)
    full_name = models.CharField('Nombre Completo', max_length=150)
    date_birth = models.DateField('Fecha de Nacimiento', blank=True, null=True)
    photo = models.ImageField('Foto de Perfil', upload_to='perfil', null=True, blank=True)
    phone = models.CharField('Telefono', max_length=15, null=True, blank=True)
    address = models.CharField('Direccion', max_length=50, null=True, blank=True)

    is_staff = models.BooleanField('Staff', default=False)
    is_active = models.BooleanField('Activo', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def get_email(self):
        return self.email
    

    def get_full_name(self):
        return self.full_name