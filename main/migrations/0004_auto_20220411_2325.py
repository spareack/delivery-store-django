# Generated by Django 3.2.12 on 2022-04-11 20:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_food_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('food_list', models.TextField()),
                ('filename', models.ImageField(default='-1.png', upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='food',
            name='file',
        ),
        migrations.RemoveField(
            model_name='food',
            name='title',
        ),
        migrations.AddField(
            model_name='food',
            name='filename',
            field=models.TextField(default='-1.png'),
        ),
        migrations.AddField(
            model_name='food',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='price',
            field=models.CharField(default=datetime.datetime(2022, 4, 11, 20, 24, 52, 594929, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='weight',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='food',
            name='description',
            field=models.TextField(),
        ),
    ]
