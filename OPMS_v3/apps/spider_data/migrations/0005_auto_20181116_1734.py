# Generated by Django 2.0.6 on 2018-11-16 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider_data', '0004_auto_20181116_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datainfo',
            name='question_text',
        ),
        migrations.AlterField(
            model_name='datalist',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
