# Generated by Django 2.2.4 on 2019-09-19 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='age',
            field=models.CharField(default=20, max_length=32),
            preserve_default=False,
        ),
    ]
