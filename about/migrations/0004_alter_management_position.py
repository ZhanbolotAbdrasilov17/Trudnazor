# Generated by Django 4.0.4 on 2022-04-15 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_structure_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='management',
            name='position',
            field=models.CharField(max_length=200, verbose_name='Должно    сть'),
        ),
    ]
