# Generated by Django 3.2.1 on 2021-05-05 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='description',
            field=models.CharField(default='Testando insercao', max_length=255),
            preserve_default=False,
        ),
    ]