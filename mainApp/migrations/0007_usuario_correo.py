# Generated by Django 5.1.3 on 2024-11-25 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_rename_iduser_usuario_idusuario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(default='gabi', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
