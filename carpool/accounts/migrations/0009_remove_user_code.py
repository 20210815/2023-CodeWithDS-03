# Generated by Django 4.2.4 on 2023-08-24 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_user_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='code',
        ),
    ]
