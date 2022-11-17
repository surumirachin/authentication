# Generated by Django 3.2.16 on 2022-11-17 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='post',
            name='time',
        ),
        migrations.AddField(
            model_name='post',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
