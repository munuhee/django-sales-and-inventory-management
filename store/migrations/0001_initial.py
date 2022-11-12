# Generated by Django 4.1.2 on 2022-10-22 08:31

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_vendor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name', unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name', unique=True)),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.FloatField(default=0.0)),
                ('original_price', models.FloatField(default=0)),
                ('selling_price', models.FloatField(default=0)),
                ('expiring_date', models.DateTimeField(blank=True, null=True)),
                ('percentage_profit', models.FloatField(verbose_name='% Profit')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.vendor')),
            ],
            options={
                'verbose_name_plural': 'Items',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.item')),
                ('avail_start_dt', models.DateField()),
                ('avail_end_dt', models.DateField(blank=True, default=datetime.date(9999, 12, 31), null=True)),
            ],
            options={
                'db_table': 'package',
            },
            bases=('store.item',),
        ),
        migrations.CreateModel(
            name='PackageItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pack_item', to='store.item')),
                ('pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pack_product', to='store.package')),
            ],
            options={
                'db_table': 'package_item',
            },
        ),
        migrations.AddField(
            model_name='package',
            name='item',
            field=models.ManyToManyField(related_name='pakage', through='store.PackageItem', to='store.item'),
        ),
    ]