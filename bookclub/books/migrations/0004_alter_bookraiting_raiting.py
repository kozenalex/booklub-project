# Generated by Django 4.1.7 on 2023-03-14 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_bookraiting_raiting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookraiting',
            name='raiting',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]