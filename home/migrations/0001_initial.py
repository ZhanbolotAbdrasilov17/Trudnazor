# Generated by Django 4.0.4 on 2022-04-13 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagline', models.CharField(max_length=500, verbose_name='Слоган')),
                ('text', models.TextField(verbose_name='Краткая информация об учереждении')),
            ],
        ),
    ]