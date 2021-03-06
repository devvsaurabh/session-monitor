# Generated by Django 2.1.7 on 2020-07-06 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.UUIDField(unique=True)),
                ('real_name', models.CharField(max_length=100)),
                ('tz', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='activityperiod',
            name='c_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity_app.User'),
        ),
    ]
