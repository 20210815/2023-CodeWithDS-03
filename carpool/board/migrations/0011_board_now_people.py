# Generated by Django 4.2.4 on 2023-08-22 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0010_alter_board_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='now_people',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
