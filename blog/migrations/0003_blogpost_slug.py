# Generated by Django 2.2.7 on 2020-01-14 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200114_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
