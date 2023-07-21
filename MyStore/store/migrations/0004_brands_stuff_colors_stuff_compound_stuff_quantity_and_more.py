# Generated by Django 4.2.2 on 2023-07-21 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_category_type_stuff_category_stuff_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='stuff',
            name='colors',
            field=models.CharField(blank=True, choices=[('White', 'White'), ('Black', 'Black')], max_length=100),
        ),
        migrations.AddField(
            model_name='stuff',
            name='compound',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='stuff',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stuff',
            name='brand',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='store.brands'),
            preserve_default=False,
        ),
    ]