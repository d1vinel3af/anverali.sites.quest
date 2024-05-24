# Generated by Django 5.0.6 on 2024-05-24 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_customuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='about',
            field=models.TextField(blank=True, default='', max_length=100, verbose_name='about'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='exp',
            field=models.CharField(blank=True, default=0, max_length=100, verbose_name='exp'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('m', 'Мужчина'), ('f', 'Женщина')], default='m', max_length=100, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profession',
            field=models.CharField(blank=True, choices=[('python', 'Python-разработчик'), ('java', 'Java-разработчик'), ('sql', 'Архитектор баз данных'), ('analytic', 'Аналитик'), ('php', 'PHP-разработчик'), ('c', 'C-разработчик')], default='', max_length=100, verbose_name='profession'),
        ),
    ]