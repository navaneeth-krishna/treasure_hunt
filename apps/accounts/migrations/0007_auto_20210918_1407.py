# Generated by Django 3.0.7 on 2021-09-18 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210917_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprogress',
            name='clue12Reached',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprogress',
            name='clue13Reached',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprogress',
            name='clue14Reached',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprogress',
            name='clue15Reached',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprogress',
            name='clue16Reached',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='wonuser',
            name='clue12Reached',
            field=models.DateTimeField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='wonuser',
            name='clue13Reached',
            field=models.DateTimeField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='wonuser',
            name='clue14Reached',
            field=models.DateTimeField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='wonuser',
            name='clue15Reached',
            field=models.DateTimeField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='wonuser',
            name='clue16Reached',
            field=models.DateTimeField(null='True'),
            preserve_default='True',
        ),
    ]
