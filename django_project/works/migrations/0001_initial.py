# Generated by Django 2.0.12 on 2020-04-29 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChallanNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challan_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='HSCNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hsc_number', models.CharField(max_length=200, verbose_name='HSN Code')),
                ('cgst', models.FloatField(verbose_name='CGST (in %)')),
                ('sgst', models.FloatField(verbose_name='SGST (in %)')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuantityRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('rate', models.FloatField()),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challan_number', models.IntegerField(unique=True)),
                ('date', models.DateField()),
                ('hsc_number', models.CharField(max_length=200)),
                ('cgst', models.FloatField()),
                ('sgst', models.FloatField()),
                ('total_amount', models.FloatField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceChallanNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_challan_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=200, null=True)),
                ('particular', models.CharField(max_length=200)),
                ('challan_number', models.IntegerField(unique=True)),
                ('date', models.DateField()),
                ('quantity', models.FloatField()),
                ('rate', models.FloatField()),
                ('amount', models.FloatField()),
                ('weight', models.CharField(blank=True, max_length=100, null=True)),
                ('scrap_weight', models.CharField(blank=True, max_length=100, null=True)),
                ('end_pieces', models.CharField(blank=True, max_length=100, null=True)),
                ('total_weight', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('amount', models.FloatField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('po_number', models.CharField(blank=True, max_length=1000, null=True)),
                ('jc_number', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='quantityrate',
            name='report',
            field=models.ManyToManyField(to='works.Report'),
        ),
    ]
