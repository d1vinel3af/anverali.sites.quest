# Generated by Django 5.0.6 on 2024-05-24 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_order_who_needs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='who_needs',
            field=models.CharField(choices=[('python', 'Python-разработчик'), ('java', 'Java-разработчик'), ('sql', 'Архитектор баз данных'), ('analytic', 'Аналитик'), ('php', 'PHP-разработчик'), ('c', 'C-разработчик')], max_length=100),
        ),
    ]
