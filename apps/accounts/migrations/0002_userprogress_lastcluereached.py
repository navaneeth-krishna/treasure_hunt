# Generated by Django 3.0.7 on 2021-05-25 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprogress',
            name='lastClueReached',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
