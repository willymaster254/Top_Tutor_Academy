# Generated by Django 4.0.1 on 2022-05-03 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_created',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
