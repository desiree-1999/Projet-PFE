# Generated by Django 5.1 on 2024-09-08 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0002_person_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='mot_de_passe',
        ),
    ]
