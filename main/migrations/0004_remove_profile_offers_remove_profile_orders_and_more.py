# Generated by Django 4.2 on 2024-04-23 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_alter_profile_offers_alter_profile_orders_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='offers',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='orders',
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='offers',
            field=models.ManyToManyField(related_name='offers', to='main.order'),
        ),
        migrations.AddField(
            model_name='profile',
            name='orders',
            field=models.ManyToManyField(related_name='orders', to='main.order'),
        ),
    ]