# Generated by Django 4.2.4 on 2023-08-23 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_merge_0002_rename_email_user_email_0002_user_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='Email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]