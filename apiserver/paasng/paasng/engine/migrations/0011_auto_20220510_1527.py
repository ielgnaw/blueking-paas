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
# Generated by Django 3.2.12 on 2022-05-10 07:27

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0010_auto_20211126_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cellpackage',
            name='engine_app',
        ),
        migrations.RemoveField(
            model_name='cellpackage',
            name='plan',
        ),
        migrations.AlterUniqueTogether(
            name='cellpackageplan',
            unique_together=None,
        ),
        migrations.AlterUniqueTogether(
            name='domain',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='domain',
            name='environment',
        ),
        migrations.RemoveField(
            model_name='domain',
            name='module',
        ),
        migrations.AlterField(
            model_name='deployment',
            name='procfile',
            field=jsonfield.fields.JSONField(default=dict, help_text='启动命令, 在准备阶段 PaaS 会从源码(或配置)读取应用的 procfile, 并更新该字段, 在发布阶段将从该字段读取 procfile'),
        ),
        migrations.AlterField(
            model_name='deployphase',
            name='type',
            field=models.CharField(choices=[('preparation', '准备阶段'), ('build', '构建阶段'), ('release', '部署阶段')], max_length=32, verbose_name='部署阶段类型'),
        ),
        migrations.AlterField(
            model_name='deploystepmeta',
            name='phase',
            field=models.CharField(choices=[('preparation', '准备阶段'), ('build', '构建阶段'), ('release', '部署阶段')], max_length=16, verbose_name='关联阶段'),
        ),
        migrations.DeleteModel(
            name='Cell',
        ),
        migrations.DeleteModel(
            name='CellPackage',
        ),
        migrations.DeleteModel(
            name='CellPackagePlan',
        ),
        migrations.DeleteModel(
            name='Domain',
        ),
    ]
