# Generated by Django 4.2.13 on 2024-07-10 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0020_rename_lang_code_hometext_en_lang_code_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HomeText',
        ),
    ]
