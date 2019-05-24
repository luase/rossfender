# Generated by Django 2.2.1 on 2019-05-22 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flavor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True)),
                ('ingredients', models.ManyToManyField(to='orders.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feeds', models.PositiveSmallIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('flavor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Flavor')),
                ('shape', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Shape')),
            ],
            options={
                'unique_together': {('shape', 'flavor')},
            },
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('units', models.CharField(choices=[('g', 'gramos(s)'), ('kg', 'kilogramo(s)')], default='g', max_length=3)),
                ('cake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Cake')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Ingredient')),
            ],
            options={
                'unique_together': {('cake', 'ingredient')},
            },
        ),
    ]
