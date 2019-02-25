# Generated by Django 2.1.3 on 2019-02-19 16:36

from django.db import migrations, models
import uploadtest.models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadtest', '0002_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, storage=uploadtest.models.OverwriteStorage(), upload_to='books/covers/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pdf',
            field=models.FileField(storage=uploadtest.models.OverwriteStorage(), upload_to='books/pdfs/'),
        ),
    ]