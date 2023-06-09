# Generated by Django 4.0.4 on 2022-05-03 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_color_size_products_size_products_specifications'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_colors', to='store.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_attrs', to='store.products')),
                ('sizes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_sizes', to='store.size')),
            ],
        ),
    ]
