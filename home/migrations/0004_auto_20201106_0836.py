# Generated by Django 3.1.3 on 2020-11-06 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201106_0807'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='banner_backgrounf_image',
            new_name='banner_background_image',
        ),
    ]
