# Generated by Django 5.0.3 on 2024-04-03 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproducts',
            name='count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
