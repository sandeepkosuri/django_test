# Generated by Django 3.2.5 on 2021-07-03 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20210703_1738'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['status']},
        ),
    ]