# Generated by Django 4.1.7 on 2023-03-01 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_tempuser'),
        ('meetings', '0003_remove_meeting_temp_users_meeting_temp_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='particepents',
            field=models.ManyToManyField(blank=True, through='meetings.MeetingToUser', to='users.myuser'),
        ),
    ]
