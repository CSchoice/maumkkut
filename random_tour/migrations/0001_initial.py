# Generated by Django 4.2.6 on 2024-09-16 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('createDB', '0002_remove_user_info_tour_like_tour_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RandomTour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='RandomTourOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
                ('random_tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='random_tour.randomtour')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='createDB.tours')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='randomtour',
            name='tour_list',
            field=models.ManyToManyField(through='random_tour.RandomTourOrder', to='createDB.tours'),
        ),
        migrations.AddField(
            model_name='randomtour',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='randomtourorder',
            constraint=models.UniqueConstraint(fields=('random_tour', 'tour'), name='unique_randomtour_tour'),
        ),
    ]
