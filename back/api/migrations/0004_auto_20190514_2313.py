# Generated by Django 2.2.1 on 2019-05-14 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190514_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='premiere',
            field=models.DateField(blank=True),
        ),
    ]
