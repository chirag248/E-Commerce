# Generated by Django 4.0.4 on 2022-05-03 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_product_attribute_sizes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='specifications',
            field=models.CharField(help_text='seperate it by ,', max_length=250, null=True),
        ),
    ]
