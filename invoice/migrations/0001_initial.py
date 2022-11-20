# Generated by Django 4.1.2 on 2022-11-18 11:04

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0005_rename_delivered_delivery_is_delivered'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='date', unique=True)),
                ('date', models.DateTimeField()),
                ('customer_name', models.CharField(max_length=30)),
                ('contact_number', models.CharField(max_length=13)),
                ('price_per_item', models.FloatField(verbose_name='Price Per Iem (Ksh)')),
                ('quantity', models.FloatField(default=0.0)),
                ('total', models.FloatField(verbose_name='Total Amount (Ksh)')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.item')),
            ],
        ),
    ]