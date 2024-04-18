# Generated by Django 5.0 on 2024-03-05 18:38

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
            name='Gents_clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('G_Cloth_name', models.TextField(unique=True)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='image/')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ladies_clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('L_Cloth_name', models.TextField(unique=True)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='image/')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phon', models.BigIntegerField()),
                ('address', models.TextField()),
                ('Users', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='cartentrties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Gentsclothes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clothstoreapp.gents_clothes')),
                ('Lediesclothes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clothstoreapp.ladies_clothes')),
            ],
        ),
    ]
