# Generated by Django 3.2.12 on 2022-10-28 04:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pluginscenter', '0003_auto_20221101_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovalService',
            fields=[
                ('uuid', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='UUID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('service_name', models.CharField(max_length=64, unique=True, verbose_name='审批服务名称')),
                ('service_id', models.IntegerField(help_text='用于在 ITSM 上提申请单据', verbose_name='审批服务ID')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
