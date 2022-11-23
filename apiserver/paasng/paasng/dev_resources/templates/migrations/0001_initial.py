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
# Generated by Django 3.2.12 on 2022-09-08 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='模板名称')),
                ('type', models.CharField(choices=[('normal', '普通应用'), ('scene', '场景模板')], max_length=16, verbose_name='模板类型')),
                ('display_name_zh_cn', models.CharField(max_length=64, verbose_name='展示用名称')),
                ('display_name_en', models.CharField(blank=True, max_length=64, verbose_name='展示用名称')),
                ('description_zh_cn', models.CharField(max_length=128, verbose_name='模板描述')),
                ('description_en', models.CharField(blank=True, max_length=128, verbose_name='模板描述')),
                ('language', models.CharField(max_length=32, verbose_name='开发语言')),
                ('market_ready', models.BooleanField(default=False, verbose_name='能否发布到应用集市')),
                ('preset_services_config', models.JSONField(blank=True, default=dict, verbose_name='预设增强服务配置')),
                ('blob_url', models.JSONField(verbose_name='不同版本二进制包存储路径')),
                ('enabled_regions', models.JSONField(blank=True, default=list, verbose_name='允许被使用的版本')),
                ('required_buildpacks', models.JSONField(blank=True, default=list, verbose_name='必须的构建工具')),
                ('tags', models.JSONField(blank=True, default=list, verbose_name='标签')),
                ('repo_url', models.CharField(default='', max_length=256, verbose_name='代码仓库信息')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
