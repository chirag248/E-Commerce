# Generated by Django 4.0.4 on 2022-05-03 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_product_attribute_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_attribute',
            name='sizes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_sizes', to='store.size'),
        ),
    ]
