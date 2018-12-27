# Generated by Django 2.0.6 on 2018-12-27 15:48

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
            name='PlatformInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='平台名称')),
                ('url', models.CharField(max_length=200, verbose_name='url')),
                ('belong', models.PositiveSmallIntegerField(choices=[(1, '公司平台'), (2, '第三方平台')], verbose_name='隶属')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, '正常'), (0, '停用')], default=1, verbose_name='状态')),
            ],
            options={
                'verbose_name': '平台表',
                'verbose_name_plural': '平台表',
            },
        ),
        migrations.CreateModel(
            name='PlatformUserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=30, null=True, verbose_name='平台名称')),
                ('password', models.CharField(blank=True, max_length=50, null=True, verbose_name='平台密码')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, '正常'), (0, '停用')], default=1, verbose_name='状态')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pu_plat', to='platform_management.PlatformInfo', verbose_name='平台')),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='platform_update_user', to=settings.AUTH_USER_MODEL, verbose_name='修改人')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pu_user', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '平台用户表',
                'verbose_name_plural': '平台用户表',
            },
        ),
    ]
