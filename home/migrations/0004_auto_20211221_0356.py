# Generated by Django 2.2.9 on 2021-12-21 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_anuncio'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Anuncio',
            new_name='Anuncios',
        ),
        migrations.AlterModelOptions(
            name='anuncios',
            options={'verbose_name': 'Anuncio', 'verbose_name_plural': 'Anuncios'},
        ),
    ]