# Generated by Django 4.2.2 on 2023-07-22 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_brands_stuff_colors_stuff_compound_stuff_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stuff',
            name='rating',
            field=models.SmallIntegerField(default=3),
            preserve_default=False,
        ),
    ]