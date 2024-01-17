# Generated by Django 4.2.8 on 2024-01-17 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsersExpenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField(null=True)),
                ('user_name', models.CharField(max_length=128, null=True)),
                ('company_name', models.CharField(max_length=256, null=True)),
                ('category_name', models.CharField(max_length=512, null=True)),
                ('price', models.FloatField(null=True)),
                ('dttm', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'users_expenses',
                'managed': False,
            },
        ),
    ]
