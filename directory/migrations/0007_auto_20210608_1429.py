# Generated by Django 3.1.7 on 2021-06-08 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0006_auto_20210608_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address_ZIP',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='address_line1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='address_line2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='address_state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
