# Generated by Django 4.2.13 on 2024-07-10 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0018_remove_hometext_sub_title_remove_hometext_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hometext',
            name='lang_code',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]