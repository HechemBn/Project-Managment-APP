# Generated by Django 2.2.24 on 2022-05-08 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taches', '0010_tache_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tache',
            name='Status',
            field=models.CharField(choices=[('To Do', 'To Do'), ('In Progress', 'In Progress'), ('Done', 'Done')], default='uncompleted', max_length=200, null=True),
        ),
    ]