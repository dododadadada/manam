# Generated by Django 4.0.3 on 2022-08-25 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0007_alter_program_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('recommendation1', models.CharField(max_length=200)),
                ('recommendation2', models.CharField(max_length=200)),
                ('recommendation3', models.CharField(max_length=200)),
                ('recommendation4', models.CharField(max_length=200)),
            ],
        ),
    ]
