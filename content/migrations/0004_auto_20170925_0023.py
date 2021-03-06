# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-25 00:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0003_remove_post_published_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': 'content_category',
            },
        ),
        migrations.CreateModel(
            name='ContentItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('body', tinymce.models.HTMLField()),
                ('description', tinymce.models.HTMLField()),
                ('thumbnail_image', models.ImageField(blank=True, upload_to='content/thumbs/')),
                ('header_image', models.ImageField(blank=True, upload_to='content/headers/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.ContentCategory')),
            ],
            options={
                'db_table': 'content_item',
            },
        ),
        migrations.CreateModel(
            name='ContentLayout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('layout_id', models.CharField(choices=[('1', 'Full Width (No Sidebar)'), ('2', 'Sidebar')], max_length=1)),
            ],
            options={
                'db_table': 'content_layout',
            },
        ),
        migrations.CreateModel(
            name='PublishHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField()),
                ('content_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.ContentItem')),
            ],
            options={
                'db_table': 'content_publish_history',
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='contenttype',
            name='name',
        ),
        migrations.AddField(
            model_name='contenttype',
            name='type_id',
            field=models.CharField(choices=[('1', 'Page'), ('2', 'Post')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='contentitem',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.ContentType'),
        ),
        migrations.AddField(
            model_name='contentitem',
            name='tags',
            field=models.ManyToManyField(to='content.ContentTag'),
        ),
    ]
