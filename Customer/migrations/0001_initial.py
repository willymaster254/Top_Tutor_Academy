# Generated by Django 4.0.1 on 2022-05-03 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import email.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('pages', models.FloatField(blank=True, null=True)),
                ('style', models.CharField(blank=True, choices=[('HARVARD', 'HARVARD'), ('APA', 'APA'), ('MLA', 'MLA'), ('CHICAGO', 'CHICAGO'), ('Any Other ', 'Any Other')], default='Select', max_length=200, null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('files', models.FileField(blank=True, max_length=255, null=True, upload_to='Upload_files/%Y%m%d/')),
                ('budget', models.FloatField(default=10)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('pages', models.FloatField(blank=True, null=True)),
                ('style', models.CharField(blank=True, choices=[('HARVARD', 'HARVARD'), ('APA', 'APA'), ('MLA', 'MLA'), ('CHICAGO', 'CHICAGO'), ('Other ', 'Other')], default='Select', max_length=200, null=True)),
                ('time', models.DateTimeField(blank=True, default=email.utils.localtime, null=True, verbose_name='Deadline ie D/M/Y Hr:Min ')),
                ('files', models.FileField(blank=True, max_length=255, null=True, upload_to='Upload_files/%Y%m%d/')),
                ('budget', models.FloatField(default=10)),
                ('date_created', models.PositiveBigIntegerField(blank=True, null=True)),
                ('answer', models.FileField(blank=True, max_length=255, null=True, upload_to='Answers/%Y%m%d/')),
                ('progress', models.BooleanField(default=False)),
                ('paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'order_with_respect_to': 'user',
            },
        ),
    ]