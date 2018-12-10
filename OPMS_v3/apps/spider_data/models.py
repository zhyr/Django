from django.db import models
from users.models import UserProfile

class FoodRank(models.Model):
    # id = models.AutoField(primary_key= True)
    tip=models.CharField(verbose_name='排行类型', max_length=100)
    tip_id=models.IntegerField(verbose_name='排行类型id')
    classifi=models.CharField(verbose_name='店铺类型', max_length=100)
    rank=models.IntegerField(verbose_name='排名')
    shopId=models.CharField(verbose_name='店铺id', max_length=100)
    shopName=models.CharField(verbose_name='店铺名', max_length=100)
    mainRegionName=models.CharField(verbose_name='所在区域', max_length=100, blank=True, null=True)
    taste=models.FloatField(verbose_name='口味', blank=True, null=True)
    environment=models.FloatField(verbose_name='环境', blank=True, null=True)
    service=models.FloatField(verbose_name='服务', blank=True, null=True)
    avgPrice=models.IntegerField(verbose_name='平均消费', blank=True, null=True)
    city_id=models.IntegerField(verbose_name='城市id')
    address=models.CharField(verbose_name='地址', max_length=300, blank=True, null=True)
    update_time=models.DateField(verbose_name='更新时间')

    class Meta:
        verbose_name = '大众点评店铺排行表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tip_id


class ZhihuList(models.Model):
    # id = models.AutoField(primary_key= True)
    question=models.CharField(verbose_name='问题标题', max_length=30)
    hot=models.CharField(verbose_name='问题热度', max_length=30)
    answer_count=models.IntegerField(verbose_name='回答数')


    class Meta:
        verbose_name = '知乎问题表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question

class ZhihuInfo(models.Model):

    question=models.ForeignKey(ZhihuList,to_field='id',verbose_name='问题标题',on_delete=models.CASCADE)
    # question_text=models.CharField(verbose_name='问题标题',max_length=300)
    text=models.CharField(verbose_name='回答内容', max_length=3000)
    author=models.CharField(verbose_name='回答作者', max_length=30)
    voteup_count=models.IntegerField(verbose_name='赞同数量', )
    comment_count=models.IntegerField(verbose_name='评论数量', )
    update_time=models.DateTimeField(verbose_name='更新时间', max_length=30)

    class Meta:
        verbose_name = '回答详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text