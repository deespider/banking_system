# Generated by Django 4.1.1 on 2022-09-25 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0026_transfers_user_alter_accholder_account_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accholder',
            name='account_number',
            field=models.IntegerField(default=916955948, unique=True),
        ),
    ]