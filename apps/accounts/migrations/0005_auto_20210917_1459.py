# Generated by Django 3.0.7 on 2021-09-17 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210917_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprogress',
            name='descq1time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprogress',
            name='descq2time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]