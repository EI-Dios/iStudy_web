# Generated by Django 2.2.14 on 2020-08-12 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('position', models.CharField(max_length=32)),
                ('company', models.CharField(choices=[('0', '北京总公司'), ('1', '西安分公司'), ('2', '深圳分公司')], max_length=32)),
                ('phone', models.CharField(max_length=11)),
                ('last_time', models.DateTimeField(blank=True, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
