# Generated by Django 2.2.1 on 2019-05-15 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_hall'),
    ]

    operations = [
        migrations.AddField(
            model_name='hall',
            name='is_reserved',
            field=models.BooleanField(default=False),
        ),
    ]
