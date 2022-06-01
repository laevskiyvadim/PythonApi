from django import forms
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


# Create your models here.
class User(AbstractUser):
    """User model."""
    id = models.AutoField(primary_key=True)
    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(_("Телефон"), max_length=12)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'first_name', 'last_name']
    objects = UserManager()


class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='users')

    class STAGE(models.TextChoices):
        Задачи = 'Задачи'
        Вработе = 'В работе'
        Тестирование = 'Тестирование'
        Завершенные = 'Завершенные'
    stageOfExecution = models.CharField(
        verbose_name='Стадия', max_length=20, choices=STAGE.choices, default='Задачи')
    startTime = models.DateField(verbose_name='Дата начала')
    endTime = models.DateField(verbose_name='Дата окончания')
    task = models.CharField(verbose_name='Задача', max_length=250)

    class Meta:
        ordering = ['id']
