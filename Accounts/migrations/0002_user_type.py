# Generated by Django 2.2.24 on 2022-03-19 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Type',
            field=models.CharField(choices=[('1', 'Chef Du Projet'), ('2', 'Utilisateur'), ('3', 'Client')], default='Chef Du Projet', max_length=100),
        ),
    ]
