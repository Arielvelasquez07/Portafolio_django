# Generated by Django 4.2 on 2024-07-03 23:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0003_alter_contacto_mensaje_cifrado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='contenido',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
