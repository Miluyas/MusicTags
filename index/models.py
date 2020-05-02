from django.db import models


# Create your models here.
class Tag(models.Model):
    tag_id = models.AutoField('序号', primary_key=True)
    tag_text = models.CharField('分类标签', max_length=10)

    def __str__(self):
        return self.tag_text

    class Meta:
        # 设置Admin界面的显示内容
        verbose_name = '歌曲分类'
        verbose_name_plural = '歌曲分类'


class Song(models.Model):
    song_id = models.AutoField('序号', primary_key=True)
    song_name = models.CharField('歌名', max_length=50)
    song_singer = models.CharField('歌手', max_length=50)
    song_time = models.CharField('时长', max_length=10)
    song_img = models.CharField('歌曲图片', max_length=20)
    song_languages = models.CharField('语种', max_length=20)
    song_lyrics = models.CharField('歌词', max_length=50, default='暂无歌词')
    song_file = models.CharField('歌曲文件', max_length=50)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.song_name

    class Meta:  # 设置Admin的显示内容
        verbose_name = '歌曲信息'
        verbose_name_plural = '歌曲信息'


class History(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name='歌名')
    history_root = models.CharField('来源作品', max_length=20, default='暂无来源')
    history_story = models.CharField('故事', max_length=200, default='暂无故事')

    class Meta:
        verbose_name='你的历史'
        verbose_name_plural='你的历史'


class Folder(models.Model):
    folder_id = models.AutoField('序号', primary_key=True)
    folder_tile = models.CharField('歌单标题', max_length=100)
    folder_user = models.CharField('用户', max_length=20)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name='歌名')

    def __str__(self):
        return self.folder_tile

    class Meta:  # 设置Admin的显示内容
        verbose_name = '歌曲信息'
        verbose_name_plural = '歌曲信息'


class Commit(models.Model):
    commit_id = models.AutoField('序号', primary_key=True)
    commit_text = models.CharField('提供内容', max_length=500)
    commit_like = models.IntegerField('支持次数', max_length=20)
    commit_user = models.ForeignKey(Folder, on_delete=models.CASCADE, verbose_name='用户')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name='歌名')

    ##有变化了
    class Meta:
        verbose_name = '歌曲评论'
        verbose_name_plural = '歌曲评论'


class Dynamic(models.Model):
    dynamic_id = models.AutoField('序号', primary_key=True)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name='歌名')
    dynamic_plays = models.IntegerField('播放次数')
    dynamic_search = models.IntegerField('搜索次数')
    dynamic_down = models.IntegerField('下载次数')

    class Meta:
        verbose_name='歌曲动态'
        verbose_name_plural='歌曲动态'
