# Generated by Django 2.2.3 on 2019-09-13 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_data_structure_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='code_block',
            name='name',
            field=models.CharField(default='single-link-node', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resource',
            name='name',
            field=models.CharField(default='single-link-node', max_length=50),
            preserve_default=False,
        ),
    ]