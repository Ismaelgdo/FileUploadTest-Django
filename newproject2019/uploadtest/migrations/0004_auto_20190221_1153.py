# Generated by Django 2.1.3 on 2019-02-21 16:53

from django.db import migrations, models
import uploadtest.models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadtest', '0003_auto_20190219_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, storage=uploadtest.models.OverwriteStorage(location='books/'), upload_to='books/covers/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pdf',
            field=models.FileField(storage=uploadtest.models.OverwriteStorage(location='books/'), upload_to='books/pdfs/'),
        ),
    ]
