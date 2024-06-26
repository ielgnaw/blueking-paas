# Generated by Django 3.2.12 on 2023-09-18 02:31

from django.db import migrations, models
import django.db.models.deletion
import paas_wl.bk_app.processes.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20230717_1958'),
        ('processes', '0003_auto_20230328_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessProbe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_type', models.CharField(max_length=255)),
                ('probe_type', models.CharField(choices=[('readiness', 'readinessProbe'), ('liveness', 'livenessProbe'), ('startup', 'startupProbe')], max_length=255)),
                ('probe_handler', paas_wl.bk_app.processes.models.ProbeHandlerField(default=dict, help_text='具体的检测机制配置，例如 httpGet 完整配置')),
                ('initial_delay_seconds', models.IntegerField(default=0)),
                ('timeout_seconds', models.PositiveIntegerField(default=1)),
                ('period_seconds', models.PositiveIntegerField(default=10)),
                ('success_threshold', models.PositiveIntegerField(default=1)),
                ('failure_threshold', models.PositiveIntegerField(default=3)),
                ('app', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='process_probe', to='api.app')),
            ],
            options={
                'unique_together': {('app', 'process_type', 'probe_type')},
            },
        ),
    ]
