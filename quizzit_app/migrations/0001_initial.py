# Generated by Django 2.2.17 on 2021-03-25 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quizID', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('difficulty', models.CharField(choices=[('EASY', 'Easy'), ('Medium', 'Medium'), ('Difficult', 'Difficult')], max_length=15)),
                ('questions', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzit_app.Category')),
            ],
            options={
                'verbose_name_plural': 'Quizzes',
            },
        ),
        migrations.CreateModel(
            name='Register_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=35)),
                ('admin', models.BooleanField(default=False)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
            ],
            options={
                'verbose_name_plural': 'Register Users',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('quizID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzit_app.Quiz')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzit_app.Register_User')),
            ],
            options={
                'verbose_name_plural': 'Records',
            },
        ),
    ]
