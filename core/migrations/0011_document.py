# Generated by Django 4.2.7 on 2024-08-18 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_socialmedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('name', models.CharField(blank=True, default='', max_length=254, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, default='', max_length=254, verbose_name='Slug')),
                ('button_text', models.CharField(blank=True, default='', max_length=254, verbose_name='Button Text')),
                ('file', models.FileField(blank=True, default='', max_length=254, upload_to='documents/', verbose_name='File')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
                'ordering': ('order',),
            },
        ),
    ]
