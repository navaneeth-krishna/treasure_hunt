# Generated by Django 3.0.7 on 2021-09-17 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210917_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprogress',
            name='descq1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprogress',
            name='descq2',
            field=models.TextField(blank=True, null=True),
        ),
    ]