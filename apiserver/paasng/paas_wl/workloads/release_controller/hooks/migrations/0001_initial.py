# -*- coding: utf-8 -*-
"""
TencentBlueKing is pleased to support the open source community by making
蓝鲸智云 - PaaS 平台 (BlueKing - PaaS System) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except
in compliance with the License. You may obtain a copy of the License at

    http://opensource.org/licenses/MIT

Unless required by applicable law or agreed to in writing, software distributed under
the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the License for the specific language governing permissions and
limitations under the License.

We undertake not to change the open source license (MIT license) applicable
to the current version of the project delivered to anyone in the future.
"""
# Generated by Django 2.2.17 on 2021-11-17 09:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0004_auto_20211022_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('uuid', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='UUID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('pre-release-hook', '发布前置指令')], max_length=32)),
                ('version', models.PositiveIntegerField()),
                ('command', models.TextField()),
                ('exit_code', models.SmallIntegerField(help_text='容器结束状态码, -1 表示未知', null=True)),
                ('status', models.CharField(choices=[('scheduled', '已调度'), ('successful', '成功'), ('failed', '失败'), ('pending', '等待'), ('interrupted', '已中断')], default='pending', max_length=12)),
                ('logs_was_ready_at', models.DateTimeField(help_text='Pod 状态就绪允许读取日志的时间', null=True)),
                ('int_requested_at', models.DateTimeField(help_text='用户请求中断的时间', null=True)),
                ('operator', models.CharField(help_text='操作者(被编码的 username), 目前该字段无意义', max_length=64)),
                ('app', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='api.App')),
                ('build', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Build')),
                ('config', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='api.Config')),
                ('output_stream', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.OutputStream')),
            ],
            options={
                'ordering': ['-created'],
                'get_latest_by': 'created',
            },
        ),
    ]