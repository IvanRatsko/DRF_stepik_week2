# Generated by Django 3.1 on 2020-08-05 16:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'набор',
                'verbose_name_plural': 'наборы',
            },
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('patronymic', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'получатель',
                'verbose_name_plural': 'получатели',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_created_datetime',
                 models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата размещения')),
                ('delivery_datetime',
                 models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата доставки')),
                ('delivery_address', models.CharField(max_length=500, verbose_name='Адрес доставки')),
                ('status', models.CharField(
                    choices=[('created', 'Создан'), ('delivered', 'Доставлен'), ('processed', 'Обрабатывается'),
                             ('cancelled', 'Отменен')], default='created', max_length=10, verbose_name='Статус')),
                ('product_set',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_set',
                                   to='testAPI_v2.productset', verbose_name='Набор')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipient',
                                                to='testAPI_v2.recipient', verbose_name='Получатель')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
            },
        ),
    ]
