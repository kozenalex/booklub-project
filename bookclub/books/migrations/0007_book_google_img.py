# Generated by Django 4.1.7 on 2023-03-07 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_book_author_alter_book_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='google_img',
            field=models.URLField(blank=True, null=True),
        ),
    ]
