# Generated by Django 2.1.8 on 2019-05-16 08:49

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
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=140)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movei',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ko', models.CharField(max_length=200)),
                ('title_en', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('poster_url', models.TextField()),
                ('genre_Action', models.BooleanField(default=True)),
                ('genre_Adventure', models.BooleanField(default=True)),
                ('genre_Animation', models.BooleanField(default=True)),
                ('genre_Comedy', models.BooleanField(default=True)),
                ('genre_Crime', models.BooleanField(default=True)),
                ('genre_Documentary', models.BooleanField(default=True)),
                ('genre_Drama', models.BooleanField(default=True)),
                ('genre_Family', models.BooleanField(default=True)),
                ('genre_Fantasy', models.BooleanField(default=True)),
                ('genre_Horror', models.BooleanField(default=True)),
                ('genre_Music', models.BooleanField(default=True)),
                ('genre_Mystery', models.BooleanField(default=True)),
                ('genre_Romance', models.BooleanField(default=True)),
                ('genre_SF', models.BooleanField(default=True)),
                ('genre_Thriller', models.BooleanField(default=True)),
                ('genre_War', models.BooleanField(default=True)),
                ('genre_Western', models.BooleanField(default=True)),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_moveis', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='movei',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movei.Movei'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
