# Generated by Django 4.2.6 on 2024-09-16 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('createDB', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_info_tour_like',
            name='tour',
        ),
        migrations.RemoveField(
            model_name='user_info_tour_like',
            name='user_info',
        ),
        migrations.RemoveField(
            model_name='user_info',
            name='tour_dislike',
        ),
        migrations.RemoveField(
            model_name='user_info',
            name='tour_like',
        ),
        migrations.DeleteModel(
            name='User_info_tour_dislike',
        ),
        migrations.DeleteModel(
            name='User_info_tour_like',
        ),
    ]
