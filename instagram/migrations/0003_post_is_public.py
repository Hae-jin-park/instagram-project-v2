# Generated by Django 4.0.10 on 2023-12-19 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_public',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]
