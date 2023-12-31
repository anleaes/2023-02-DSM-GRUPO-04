# Generated by Django 4.2.7 on 2023-12-04 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('type', models.CharField(choices=[('H', 'healing'), ('D', 'damage')], max_length=1, verbose_name='Tipo')),
                ('duration', models.IntegerField(verbose_name='Duração')),
                ('base_power', models.IntegerField(verbose_name='Poder base')),
            ],
            options={
                'verbose_name_plural': 'Effects',
                'ordering': ['name'],
            },
        ),
    ]
