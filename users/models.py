from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class ProfessionChoices(models.TextChoices):
        pd = ('python', 'Python-разработчик')
        jd = ('java', 'Java-разработчик')
        sql = ('sql', 'Архитектор баз данных')
        analytic = ('analytic', 'Аналитик')
        phpd = ('php', 'PHP-разработчик')
        cd = ('c', 'C-разработчик')
    gender_choices = (
        ('m', 'Мужчина'),
        ('f', 'Женщина'),
    )
    avatar = models.ImageField(upload_to='avatars', default='avatars/default.png')
    first_name = models.CharField("first name", max_length=30)
    last_name = models.CharField("last name", max_length=30)
    email = models.EmailField("email")
    gender = models.CharField("gender", max_length=100, choices=gender_choices, default='m')
    profession = models.CharField('profession', max_length=100, blank=True, default='', choices=ProfessionChoices.choices)
    exp = models.CharField('exp', blank=True, max_length=100, default=0)
    about = models.TextField("about", default='', max_length=100, blank=True)
    telegram = models.CharField("tg", max_length=64, default='', blank=True)
    vk = models.URLField("vk", default='', blank=True)

    REQUIRED_FIELDS = ["email", "first_name", "last_name", "gender", "profession"]
