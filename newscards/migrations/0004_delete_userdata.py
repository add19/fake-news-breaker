# Generated by Django 2.0.3 on 2018-03-24 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newscards', '0003_userdata'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserData',
        ),
    ]