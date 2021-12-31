# Generated by Django 2.2.9 on 2021-12-31 17:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='depoimentos',
            name='criado',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='depoimentos',
            name='modificado',
            field=models.DateTimeField(auto_now=True),
        ),
    ]