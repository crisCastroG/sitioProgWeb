# Generated by Django 5.0.6 on 2024-06-30 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0011_rename_nro_carro_carrocompra_codigo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='estado_pedido',
            field=models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('CANCELADO', 'Cancelado'), ('ENVIADO', 'Enviado')], default='Pendiente', max_length=10),
        ),
    ]
