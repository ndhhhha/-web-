# Generated by Django 5.1.7 on 2025-04-05 17:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_app', '0011_alter_user_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='文章标题')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_contents', to='user_app.user', verbose_name='用户')),
            ],
            options={
                'verbose_name': '文章内容',
                'verbose_name_plural': '文章内容',
                'db_table': 'chat_content',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=200, verbose_name='评论内容')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('chat_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='chat_app.chatcontent', verbose_name='文章')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='user_app.user', verbose_name='用户')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'db_table': 'comment',
                'ordering': ['-created_at'],
            },
        ),
    ]
