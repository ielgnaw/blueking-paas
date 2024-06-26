# Generated by Django 3.2.12 on 2023-08-07 09:30

import blue_krill.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingress', '0005_auto_20221212_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appdomaincert',
            name='cert_data',
            field=blue_krill.models.fields.EncryptField(),
        ),
        migrations.AlterField(
            model_name='appdomaincert',
            name='key_data',
            field=blue_krill.models.fields.EncryptField(),
        ),
        migrations.AlterField(
            model_name='appdomainsharedcert',
            name='cert_data',
            field=blue_krill.models.fields.EncryptField(),
        ),
        migrations.AlterField(
            model_name='appdomainsharedcert',
            name='key_data',
            field=blue_krill.models.fields.EncryptField(),
        ),
    ]
