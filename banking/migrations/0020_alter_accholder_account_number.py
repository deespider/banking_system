# Generated by Django 4.1.1 on 2022-09-23 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0019_alter_accholder_account_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accholder',
            name='account_number',
            field=models.IntegerField(default=856605664, unique=True),
        ),
    ]
