# Generated by Django 4.2.7 on 2023-12-04 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('itemcategories', '0001_initial'),
        ('rarities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('value', models.FloatField(verbose_name='Valor')),
                ('weight', models.FloatField(verbose_name='Peso')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='itemcategories.itemcategory')),
                ('rarity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rarities.rarity')),
            ],
            options={
                'verbose_name_plural': 'Items',
                'ordering': ['name'],
            },
        ),
    ]