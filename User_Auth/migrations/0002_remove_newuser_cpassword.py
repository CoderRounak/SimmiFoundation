# Generated by Django 4.0.5 on 2022-07-28 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User_Auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='cpassword',
        ),
    ]