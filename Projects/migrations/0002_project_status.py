# Generated by Django 2.2.24 on 2022-03-23 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='Status',
            field=models.CharField(choices=[('A faire', 'A faire'), ('En cours', 'En cours'), ('Terminé', 'Terminé')], max_length=200, null=True),
        ),
    ]
