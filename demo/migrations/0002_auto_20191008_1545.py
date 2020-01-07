# Generated by Django 2.2.6 on 2019-10-08 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rendicionestado',
            name='estado',
            field=models.CharField(choices=[('CR', 'Creado'), ('RE', 'Rechazado'), ('AP', 'Aprobado')], default='CR', max_length=2),
        ),
        migrations.AlterField(
            model_name='rendicion',
            name='centro',
            field=models.ForeignKey(help_text='Seleccione el centro al cual corresponde', on_delete=django.db.models.deletion.CASCADE, to='demo.Centro', verbose_name='Centro'),
        ),
        migrations.AlterField(
            model_name='rendicion',
            name='comprobante',
            field=models.ImageField(help_text='Suba el comprobante de la compra', upload_to='boletas/', verbose_name='Comprobante'),
        ),
        migrations.AlterField(
            model_name='rendicion',
            name='monto',
            field=models.IntegerField(help_text='Ingrese un monto', verbose_name='Monto'),
        ),
        migrations.AlterField(
            model_name='rendicion',
            name='tipo_de_gasto',
            field=models.CharField(help_text='Ingrese el tipo de gasto', max_length=50, verbose_name='Tipos de gasto'),
        ),
    ]