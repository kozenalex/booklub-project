# Generated by Django 4.1.7 on 2023-03-23 13:47

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_bookraiting_raiting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.ImageField(blank=True, storage=django.core.files.storage.FileSystemStorage(location='/media/books'), upload_to='books/%Y-%m-%d/', verbose_name='Обложка'),
        ),
    ]
