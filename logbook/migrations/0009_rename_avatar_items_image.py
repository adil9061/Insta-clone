# Generated by Django 4.0 on 2023-04-28 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0008_remove_items_image_items_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='avatar',
            new_name='image',
        ),
    ]