# Generated by Django 2.1.8 on 2019-05-14 09:14

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, max_length=40)),
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
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]