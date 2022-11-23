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
# Generated by Django 2.2.17 on 2021-10-22 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210804_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='artifact_deleted',
            field=models.BooleanField(default=False, help_text='slug是否已被清理'),
        ),
        migrations.AlterField(
            model_name='build',
            name='slug_path',
            field=models.TextField(help_text='slug path 形如 {region}/home/{name}:{branch}:{revision}/push'),
        ),
        migrations.AlterField(
            model_name='buildprocess',
            name='status',
            field=models.CharField(choices=[('scheduled', 'SCHEDULED'), ('successful', 'SUCCESSFUL'), ('failed', 'FAILED'), ('pending', 'PENDING'), ('interrupted', 'INTERRUPTED')], default='pending', max_length=12),
        ),
    ]
