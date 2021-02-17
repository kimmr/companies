# Generated by Django 3.1.6 on 2021-02-17 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_companies', '0002_auto_20210217_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='is_nasdaq',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='company',
            name='symbol',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
