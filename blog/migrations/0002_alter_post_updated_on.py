# Generated by Django 3.2.14 on 2022-07-27 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
