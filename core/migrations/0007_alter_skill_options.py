# Generated by Django 4.2.7 on 2023-12-23 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_skill_alter_imagesetting_created_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ('order',), 'verbose_name': 'Skill', 'verbose_name_plural': 'Skill'},
        ),
    ]
