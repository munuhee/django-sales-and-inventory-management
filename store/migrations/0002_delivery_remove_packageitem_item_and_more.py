# Generated by Django 4.1.2 on 2022-10-22 10:51

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, max_length=30, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('location', models.CharField(blank=True, max_length=20, null=True)),
                ('date', models.DateTimeField()),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.item')),
            ],
        ),
        migrations.RemoveField(
            model_name='packageitem',
            name='item',
        ),
        migrations.RemoveField(
            model_name='packageitem',
            name='pack',
        ),
        migrations.DeleteModel(
            name='Package',
        ),
        migrations.DeleteModel(
            name='PackageItem',
        ),
    ]