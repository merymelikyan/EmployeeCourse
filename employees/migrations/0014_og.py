# Generated by Django 4.2.13 on 2024-07-01 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0013_seo'),
    ]

    operations = [
        migrations.CreateModel(
            name='OG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=500)),
                ('tipe', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='og')),
                ('url', models.ImageField(max_length=255, upload_to='')),
            ],
        ),
    ]
