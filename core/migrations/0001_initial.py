# Generated by Django 5.1 on 2024-08-23 03:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fiscal_year', models.CharField(choices=[('2081-82', '2081-82')], default='2081-82', max_length=7)),
                ('party_name', models.CharField(max_length=255)),
                ('payment_mode', models.CharField(choices=[('Cash', 'Cash'), ('Credit Card', 'Credit Card'), ('Cheque', 'Cheque')], default='Cash', max_length=11)),
                ('party_pan', models.CharField(max_length=9)),
                ('address', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('particulars', models.CharField(max_length=255)),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('date', models.DateField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.customer')),
                ('sales', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sales')),
            ],
        ),
    ]
