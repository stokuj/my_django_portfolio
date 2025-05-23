# Generated by Django 5.1.7 on 2025-05-17 10:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('thumbnail', models.ImageField(blank=True, default='thumbnails/default_image.png', null=True, upload_to='thumbnails/')),
                ('short_description', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date(2022, 5, 1))),
                ('blog', models.BooleanField(default=True)),
                ('blog_url', models.CharField(blank=True, max_length=100, null=True)),
                ('github_url', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('planned', 'Planned'), ('ongoing', 'Ongoing'), ('finished', 'Finished')], default='planned', max_length=10)),
                ('tags', models.ManyToManyField(blank=True, to='main.tag')),
            ],
        ),
    ]
