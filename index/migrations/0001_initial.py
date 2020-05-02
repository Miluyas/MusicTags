# Generated by Django 2.2.1 on 2020-05-01 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('tag_text', models.CharField(max_length=10, verbose_name='分类标签')),
            ],
            options={
                'verbose_name': '歌曲分类',
                'verbose_name_plural': '歌曲分类',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('song_name', models.CharField(max_length=50, verbose_name='歌名')),
                ('song_singer', models.CharField(max_length=50, verbose_name='歌手')),
                ('song_time', models.CharField(max_length=10, verbose_name='时长')),
                ('song_img', models.CharField(max_length=20, verbose_name='歌曲图片')),
                ('song_languages', models.CharField(max_length=20, verbose_name='语种')),
                ('song_lyrics', models.CharField(default='暂无歌词', max_length=50, verbose_name='歌词')),
                ('song_file', models.CharField(max_length=50, verbose_name='歌曲文件')),
                ('tag', models.ManyToManyField(to='index.Tag')),
            ],
            options={
                'verbose_name': '歌曲信息',
                'verbose_name_plural': '歌曲信息',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history_root', models.CharField(default='暂无来源', max_length=20, verbose_name='来源作品')),
                ('history_story', models.CharField(default='暂无故事', max_length=200, verbose_name='故事')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Song', verbose_name='歌名')),
            ],
            options={
                'verbose_name': '你的历史',
                'verbose_name_plural': '你的历史',
            },
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('folder_id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('folder_tile', models.CharField(max_length=100, verbose_name='歌单标题')),
                ('folder_user', models.CharField(max_length=20, verbose_name='用户')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Song', verbose_name='歌名')),
            ],
            options={
                'verbose_name': '歌曲信息',
                'verbose_name_plural': '歌曲信息',
            },
        ),
        migrations.CreateModel(
            name='Dynamic',
            fields=[
                ('dynamic_id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('dynamic_plays', models.IntegerField(verbose_name='播放次数')),
                ('dynamic_search', models.IntegerField(verbose_name='搜索次数')),
                ('dynamic_down', models.IntegerField(verbose_name='下载次数')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Song', verbose_name='歌名')),
            ],
            options={
                'verbose_name': '歌曲动态',
                'verbose_name_plural': '歌曲动态',
            },
        ),
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('commit_id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('commit_text', models.CharField(max_length=500, verbose_name='提供内容')),
                ('commit_like', models.IntegerField(max_length=20, verbose_name='支持次数')),
                ('commit_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Folder', verbose_name='用户')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Song', verbose_name='歌名')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Tag')),
            ],
            options={
                'verbose_name': '歌曲评论',
                'verbose_name_plural': '歌曲评论',
            },
        ),
    ]
