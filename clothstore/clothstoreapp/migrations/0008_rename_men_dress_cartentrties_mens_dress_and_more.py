# Generated by Django 5.0 on 2024-03-16 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothstoreapp', '0007_rename_dres_cartentrties_men_dress_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartentrties',
            old_name='Men_dress',
            new_name='mens_dress',
        ),
        migrations.RenameField(
            model_name='cartentrties',
            old_name='wamens_dress',
            new_name='womens_dress',
        ),
    ]