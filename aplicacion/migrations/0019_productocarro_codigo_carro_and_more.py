# Generated by Django 5.0.6 on 2024-07-01 05:52

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0018_alter_pedido_estado_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='productocarro',
            name='codigo_carro',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='aplicacion.carrocompra'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productocarro',
            name='codigo_producto',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999999999)]),
        ),
    ]