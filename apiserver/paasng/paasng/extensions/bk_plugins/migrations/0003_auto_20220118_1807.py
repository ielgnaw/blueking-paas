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
# Generated by Django 2.2.17 on 2022-01-18 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bk_plugins', '0002_auto_20220112_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='bkpluginprofile',
            name='api_gw_id',
            field=models.IntegerField(null=True, verbose_name='已绑定的 API 网关 ID'),
        ),
        migrations.AddField(
            model_name='bkpluginprofile',
            name='api_gw_last_synced_at',
            field=models.DateTimeField(null=True, verbose_name='最近一次同步网关的时间'),
        ),
        migrations.AddField(
            model_name='bkpluginprofile',
            name='api_gw_name',
            field=models.CharField(blank=True, help_text='为空时表示从未成功同步过，暂无已绑定网关', max_length=32, null=True, verbose_name='已绑定的 API 网关名称'),
        ),
    ]
