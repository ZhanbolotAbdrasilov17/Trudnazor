# Generated by Django 4.0.4 on 2022-05-30 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('other', '0003_categorycontact_remove_contact_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество')),
                ('email', models.CharField(max_length=100, verbose_name='Почта')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('text', models.TextField(verbose_name='Текст')),
                ('file', models.FileField(upload_to='email_files', verbose_name='Файл')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Обращение',
                'verbose_name_plural': 'Обращения',
                'ordering': ['-id'],
            },
        ),
    ]
