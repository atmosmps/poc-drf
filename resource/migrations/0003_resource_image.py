# Generated by Django 3.2.7 on 2021-09-21 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0002_alter_resource_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='resource'),
        ),
    ]