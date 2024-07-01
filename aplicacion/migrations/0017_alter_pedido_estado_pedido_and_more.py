# Generated by Django 5.0.6 on 2024-07-01 05:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0016_alter_pedido_estado_pedido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado_pedido',
            field=models.CharField(choices=[('CANCELADO', 'Cancelado'), ('ENVIADO', 'Enviado'), ('PENDIENTE', 'Pendiente')], default='Pendiente', max_length=10),
        ),
        migrations.AlterField(
            model_name='productocarro',
            name='codigo_producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aplicacion.carrocompra'),
        ),
    ]