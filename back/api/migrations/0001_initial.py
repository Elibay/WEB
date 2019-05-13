# Generated by Django 2.2.1 on 2019-05-13 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('poster', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('desciption', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Кинотеатр',
                'verbose_name_plural': 'Кинотеатры',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('poster', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200)),
                ('premiere', models.DateField(null=True)),
                ('duration', models.PositiveIntegerField(null=True)),
                ('age', models.PositiveIntegerField(default=18)),
                ('desc', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fixture', models.DateTimeField()),
                ('adult_price', models.PositiveIntegerField(null=True)),
                ('child_price', models.PositiveIntegerField(blank=True, null=True)),
                ('student_price', models.PositiveIntegerField(null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='schedule', to='api.Movie')),
            ],
            options={
                'verbose_name': 'Список',
                'verbose_name_plural': 'Списки',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200, null=True)),
                ('text', models.TextField(max_length=200, null=True)),
                ('date', models.DateTimeField(null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.Movie')),
            ],
            options={
                'verbose_name': 'Коммент',
                'verbose_name_plural': 'Комменты',
            },
        ),
    ]