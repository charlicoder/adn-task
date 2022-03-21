# Generated by Django 4.0.3 on 2022-03-21 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_remove_attendanceurltoken_created_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendanceurltoken',
            name='id',
        ),
        migrations.AlterField(
            model_name='attendanceurltoken',
            name='url_token',
            field=models.CharField(editable=False, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]