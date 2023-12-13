# Generated by Django 4.2.7 on 2023-12-13 20:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_imagesetting_options_imagesetting_created_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('name', models.CharField(blank=True, default='', help_text='Ayar İsmi', max_length=254, verbose_name='Name Test')),
                ('percentage', models.IntegerField(default=50, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Percentage')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='imagesetting',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
