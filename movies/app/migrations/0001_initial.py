# Generated by Django 2.2.16 on 2022-05-12 12:13

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('Title', models.CharField(blank=True, max_length=400, null=True)),
                ('Year', models.CharField(blank=True, max_length=400, null=True)),
                ('Rated', models.CharField(blank=True, max_length=400, null=True)),
                ('Released', models.CharField(blank=True, max_length=400, null=True)),
                ('Runtime', models.CharField(blank=True, max_length=400, null=True)),
                ('Genre', models.CharField(blank=True, max_length=400, null=True)),
                ('Director', models.CharField(blank=True, max_length=400, null=True)),
                ('Writer', models.CharField(blank=True, max_length=400, null=True)),
                ('Actors', models.CharField(blank=True, max_length=400, null=True)),
                ('Language', models.CharField(blank=True, max_length=400, null=True)),
                ('Country', models.CharField(blank=True, max_length=400, null=True)),
                ('Awards', models.CharField(blank=True, max_length=400, null=True)),
                ('Poster', models.TextField(blank=True, null=True)),
                ('Ratings', models.CharField(blank=True, max_length=400, null=True)),
                ('Metascore', models.CharField(blank=True, max_length=400, null=True)),
                ('imdbRating', models.CharField(blank=True, max_length=400, null=True)),
                ('imdbVotes', models.CharField(blank=True, max_length=400, null=True)),
                ('imdbID', models.CharField(blank=True, max_length=400, null=True)),
                ('Type', models.CharField(blank=True, max_length=400, null=True)),
                ('DVD', models.CharField(blank=True, max_length=100, null=True)),
                ('BoxOffice', models.CharField(blank=True, max_length=400, null=True)),
                ('Production', models.CharField(blank=True, max_length=400, null=True)),
                ('Website', models.CharField(blank=True, max_length=400, null=True)),
                ('Plot', models.TextField(blank=True, null=True)),
                ('Response', models.CharField(blank=True, max_length=400, null=True)),
                ('totalSeasons', models.CharField(blank=True, max_length=400, null=True)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('body', models.TextField()),
                ('movie', models.ForeignKey(blank=True, help_text='Movie relation', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='app.Movie')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]