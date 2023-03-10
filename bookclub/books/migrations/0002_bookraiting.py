# Generated by Django 4.1.7 on 2023-03-14 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_tempuser_telegram'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookRaiting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raiting', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.myuser')),
            ],
        ),
    ]
