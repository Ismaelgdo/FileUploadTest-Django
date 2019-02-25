# Generated by Django 2.1.3 on 2019-02-25 17:17

from django.db import migrations, models
import uploadtest.models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadtest', '0008_auto_20190225_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pdf',
            field=models.FileField(storage=uploadtest.models.OverwriteStorage(), upload_to='books/pdfs'),
        ),
    ]