# Generated by Django 3.2 on 2022-07-15 21:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20220716_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2022, 7, 15, 21, 36, 53, 564445, tzinfo=utc)),
        ),
    ]