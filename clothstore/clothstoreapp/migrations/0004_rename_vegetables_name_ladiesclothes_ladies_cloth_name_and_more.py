# Generated by Django 5.0 on 2024-03-06 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothstoreapp', '0003_rename_vegetables_ladiesclothes_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ladiesclothes',
            old_name='vegetables_name',
            new_name='Ladies_cloth_name',
        ),
        migrations.RenameField(
            model_name='mensclothes',
            old_name='fruit_name',
            new_name='Men_cloth_name',
        ),
    ]
