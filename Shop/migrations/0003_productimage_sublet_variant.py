# Generated by Django 2.2.4 on 2019-08-06 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_auto_20190806_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=150)),
                ('desc', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Sublet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=150)),
                ('color_hex', models.CharField(max_length=6)),
                ('max_retail_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.Variant')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(max_length=700)),
                ('caption', models.CharField(max_length=50)),
                ('sublet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.Sublet')),
            ],
        ),
    ]