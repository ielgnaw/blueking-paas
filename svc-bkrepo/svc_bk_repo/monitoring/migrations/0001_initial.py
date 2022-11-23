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
# Generated by Django 3.2.12 on 2022-06-30 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paas_service', '0008_auto_20220426_0429'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepoQuotaStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo_name', models.CharField(max_length=64, verbose_name='仓库名称')),
                ('max_size', models.IntegerField(help_text='单位字节，值为 nul 时表示未设置仓库配额', null=True, verbose_name='仓库最大配额')),
                ('used', models.IntegerField(default=0, help_text='单位字节', verbose_name='仓库已使用容量')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('instance', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='paas_service.serviceinstance')),
            ],
        ),
    ]
