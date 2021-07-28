# Generated by Django 1.9.13 on 2017-08-31 05:44

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import markupfield.fields


class Migration(migrations.Migration):

    replaces = [('community', '0001_initial'), ('community', '0002_auto_20150416_1853'), ('community', '0003_auto_20170831_0358'), ('community', '0004_auto_20170831_0541')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, db_index=True, default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('url', models.URLField(blank=True, max_length=1000, verbose_name='URL')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community_link_creator', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community_link_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Links',
                'ordering': ['-created'],
                'verbose_name': 'Link',
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, db_index=True, default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('image', models.ImageField(blank=True, upload_to='community/photos/')),
                ('image_url', models.URLField(blank=True, max_length=1000, verbose_name='Image URL')),
                ('caption', models.TextField(blank=True)),
                ('click_through_url', models.URLField(blank=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community_photo_creator', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community_photo_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'photos',
                'ordering': ['-created'],
                'verbose_name': 'photo',
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, db_index=True, default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('content', markupfield.fields.MarkupField(rendered_field=True)),
                ('abstract', models.TextField(blank=True, null=True)),
                ('content_markup_type', models.CharField(choices=[('', '--'), ('html', 'html'), ('plain', 'plain'), ('markdown', 'markdown'), ('restructuredtext', 'restructuredtext')], default='html', max_length=30)),
                ('_content_rendered', models.TextField(editable=False)),
                ('media_type', models.IntegerField(choices=[(1, 'text'), (2, 'photo'), (3, 'video'), (4, 'link')], default=1)),
                ('source_url', models.URLField(blank=True, max_length=1000)),
                ('meta', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={})),
                ('status', models.IntegerField(choices=[(1, 'private'), (2, 'public')], db_index=True, default=1)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community_post_creator', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community_post_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'posts',
                'ordering': ['-created'],
                'verbose_name': 'post',
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, db_index=True, default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('video_embed', models.TextField(blank=True)),
                ('video_data', models.FileField(blank=True, upload_to='community/videos/')),
                ('caption', models.TextField(blank=True)),
                ('click_through_url', models.URLField(blank=True, verbose_name='Click Through URL')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community_video_creator', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community_video_modified', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_video', to='community.Post')),
            ],
            options={
                'verbose_name_plural': 'videos',
                'ordering': ['-created'],
                'verbose_name': 'video',
                'get_latest_by': 'created',
            },
        ),
        migrations.AddField(
            model_name='photo',
            name='post',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_photo', to='community.Post'),
        ),
        migrations.AddField(
            model_name='link',
            name='post',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_link', to='community.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_markup_type',
            field=models.CharField(choices=[('', '--'), ('html', 'HTML'), ('plain', 'Plain'), ('markdown', 'Markdown'), ('restructuredtext', 'Restructured Text')], default='html', max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='meta',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}),
        ),
        migrations.AlterField(
            model_name='post',
            name='meta',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
    ]
