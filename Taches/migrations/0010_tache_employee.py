# Generated by Django 2.2.24 on 2022-05-06 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Taches', '0009_auto_20220506_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='tache',
            name='Employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
