# Generated by Django 5.0.3 on 2024-04-03 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_orderproducts_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='percent',
            field=models.PositiveIntegerField(),
        ),
    ]
