# Generated by Django 5.1.6 on 2025-03-05 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='blog/images')),
                ('url', models.URLField(blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
