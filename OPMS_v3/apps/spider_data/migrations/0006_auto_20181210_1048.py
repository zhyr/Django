# Generated by Django 2.0.6 on 2018-12-10 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spider_data', '0005_auto_20181116_1734'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DataInfo',
            new_name='ZhihuInfo',
        ),
        migrations.RenameModel(
            old_name='DataList',
            new_name='ZhihuList',
        ),
    ]