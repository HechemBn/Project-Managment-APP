# Generated by Django 2.2.24 on 2022-03-19 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255, verbose_name='Titre du projet')),
                ('Description', models.TextField(max_length=800, verbose_name='Description du projet')),
                ('StartDate', models.DateField(max_length=100, verbose_name='Date de début')),
                ('EndDate', models.DateField(max_length=100, verbose_name='Date de fin')),
                ('ProjectManager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
