# Generated by Django 4.2.3 on 2023-07-05 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_product_productdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetail',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
