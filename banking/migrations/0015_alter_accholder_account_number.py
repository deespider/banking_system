# Generated by Django 4.1.1 on 2022-09-22 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0014_alter_accholder_account_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accholder',
            name='account_number',
            field=models.IntegerField(default=492034290, unique=True),
        ),
    ]
