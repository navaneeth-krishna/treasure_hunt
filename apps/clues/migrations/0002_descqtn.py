# Generated by Django 3.0.7 on 2021-09-17 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clues', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescQtn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_no', models.IntegerField(default=0)),
                ('question', models.TextField()),
            ],
        ),
    ]