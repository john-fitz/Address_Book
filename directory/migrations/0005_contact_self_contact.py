# Generated by Django 3.1.7 on 2021-06-01 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0004_contact_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='self_contact',
            field=models.BooleanField(default=False),
        ),
    ]
