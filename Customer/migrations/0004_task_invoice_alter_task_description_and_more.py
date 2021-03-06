# Generated by Django 4.0.1 on 2022-05-10 06:10

from django.db import migrations, models
import email.utils


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0003_rename_date_created_task_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='invoice',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='progress',
            field=models.BooleanField(default=False, verbose_name='Mark as Complete'),
        ),
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.DateTimeField(blank=True, default=email.utils.localtime, null=True, verbose_name='Deadline ie D-Y-M Hr:Min:Sec '),
        ),
    ]
