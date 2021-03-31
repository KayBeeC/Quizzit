# Generated by Django 2.2.17 on 2021-03-31 14:57

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
                ('name', models.CharField(max_length=50, unique=True)),
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
                ('name', models.CharField(max_length=50)),
                ('difficulty', models.CharField(choices=[('EASY', 'Easy'), ('MEDIUM', 'Medium'), ('HARD', 'Hard')], max_length=10)),
                ('views', models.IntegerField(default=0)),
                ('quizID', models.CharField(blank=True, max_length=10, unique=True)),
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
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
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
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzit_app.Quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzit_app.Register_User')),
            ],
            options={
                'verbose_name_plural': 'Records',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('question_text', models.CharField(max_length=500)),
                ('choiceA', models.CharField(max_length=200)),
                ('choiceB', models.CharField(max_length=200)),
                ('choiceC', models.CharField(max_length=200)),
                ('choiceD', models.CharField(max_length=200)),
                ('answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzit_app.Quiz')),
            ],
            options={
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.AddConstraint(
            model_name='quiz',
            constraint=models.UniqueConstraint(fields=('name', 'difficulty', 'category'), name='unique quiz constraint'),
        ),
        migrations.AddConstraint(
            model_name='quiz',
            constraint=models.CheckConstraint(check=models.Q(difficulty__in=['EASY', 'MEDIUM', 'HARD']), name='difficulty validity constraint'),
        ),
        migrations.AddConstraint(
            model_name='question',
            constraint=models.UniqueConstraint(fields=('index', 'quiz'), name='unique question constraint'),
        ),
        migrations.AddConstraint(
            model_name='question',
            constraint=models.CheckConstraint(check=models.Q(answer__in=['A', 'B', 'C', 'D']), name='answer validity constraint'),
        ),
    ]
