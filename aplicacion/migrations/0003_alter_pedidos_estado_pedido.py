# Generated by Django 5.0.6 on 2024-06-24 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_cliente_imagen_alter_pedidos_estado_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='estado_pedido',
            field=models.CharField(choices=[('CANCELADO', 'Cancelado'), ('ENVIADO', 'Enviado'), ('PENDIENTE', 'Pendiente')], max_length=10),
        ),
    ]